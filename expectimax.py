'''Single player Expectimax algorithm for Balatro
Authors: Joshua Moellers'''
import random

def run_expectimax(game, depth=2, sample=10):
    while not game.is_over:
        actions = game.gen_actions()
        actions = [a for a in actions if "MoveCard" not in str(a)]
        random.shuffle(actions)
        actions = actions if sample == -1 else actions[:sample]

        best_score = -float('inf')
        best_action = actions[0]

        for action in actions:
            new_game = game.clone()
            new_game.handle_action(action)

            score = value(new_game, depth, sample, previous_score=game.state.score)

            if score > best_score:
                best_score = score
                best_action = action
        
        # print("action:", best_action)
        # before = game.state.score
        game.handle_action(best_action)
        # after = game.state.score
        # print("score delta:", after - before)

    return game.state.score, game.is_win, game.state

def value(game, depth, sample, previous_score=0):
    if game.is_over or depth <= 0:
        return heuristic(game, game.state.score - previous_score)
    
    return max_value(game, depth, sample, previous_score=previous_score)

def max_value(game, depth, sample, previous_score=0):
    best = -float('inf')
    actions = game.gen_actions()
    actions = [a for a in actions if "MoveCard" not in str(a)]
    random.shuffle(actions)
    actions = actions if sample == -1 else actions[:sample]

    for action in actions:
        val = chance_value(game, action, depth - 1, sample, previous_score=previous_score)
        best = max(best, val)

    return best

def chance_value(game, action, depth, sample, previous_score=0):
    chance_sample_size = 3
    total = 0

    for _ in range(chance_sample_size):
        new_game = game.clone()
        new_game.handle_action(action)
        total += value(new_game, depth, sample, previous_score=previous_score)

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
