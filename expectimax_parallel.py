'''Single player Expectimax parellel thread algorithm for Balatro
Authors: Joshua Moellers'''
import random
from concurrent.futures import ThreadPoolExecutor

def root_branch_eval(game, action, depth, sample, executor):
    game.handle_action(action)
    return value(game, depth, sample, executor, previous_score=game.state.score)

def run_expectimax(game, depth=2, sample=10):
    with ThreadPoolExecutor() as executor:
        while not game.is_over:
            actions = game.gen_actions()
            actions = [a for a in actions if "MoveCard" not in str(a)]
            random.shuffle(actions)
            actions = actions if sample == -1 else actions[:sample]

            futures = []
            for action in actions:
                new_game = game.clone()
                futures.append(executor.submit(root_branch_eval, new_game, action, depth, sample, executor))

            results = [f.result() for f in futures]

            best_score, best_idx = max((val, i) for i, val in enumerate(results))
            best_action = actions[best_idx]
            
            # print("action:", best_action)
            # before = game.state.score
            game.handle_action(best_action)
            # after = game.state.score
            # print("score delta:", after - before)

        return game.state.score, game.is_win, game.state

def value(game, depth, sample, executor, previous_score=0):
    if game.is_over or depth <= 0:
        return heuristic(game, game.state.score - previous_score)
    
    return max_value(game, depth, sample, executor, previous_score=previous_score)

def max_value(game, depth, sample, executor, previous_score=0):
    best = -float('inf')
    actions = game.gen_actions()
    actions = [a for a in actions if "MoveCard" not in str(a)]
    random.shuffle(actions)
    actions = actions if sample == -1 else actions[:sample]

    for action in actions:
        val = chance_value(game, action, depth - 1, sample, executor, previous_score=previous_score)
        best = max(best, val)

    return best

def chance_value(game, action, depth, sample, executor, previous_score=0):
    chance_sample_size = 3
    total = 0

    for _ in range(chance_sample_size):
        new_game = game.clone()
        new_game.handle_action(action)
        total += value(new_game, depth, sample, executor, previous_score=previous_score)

    return total / chance_sample_size

def heuristic(game, diff):
    # Terminal state
    if game.is_over:
        return 1e9 if game.is_win else -1e9
    
    state = game.state
    value = state.score
    value += state.score / (state.required_score + 1) * 100
    value += state.plays * 100
    value += state.discards * 50
    value -= len(state.action_history) * 10
    
    return value
