'''Single player Expectimax algorithm for Balatro
Authors: Joshua Moellers'''
import time

SAMPLE = 10 # To limit the branching factor

def run_expectimax(game, depth=2):
    #print("Running run_expectimax...")
    while not game.is_over:
        actions = game.gen_actions()
        best_score = -float('inf')
        best_action = actions[0]

        for action in actions[:SAMPLE]:
            new_game = game.clone()
            new_game.handle_action(action)

            score = value(new_game, depth)

            if score > best_score:
                best_score = score
                best_action = action
        
        game.handle_action(best_action)

    #print("Finished run_expectimax")
    return game.state.score, game.is_win

def value(game, depth):
    #print("Running value...")
    if game.is_over or depth == 0:
        return heuristic(game)
    
    return max_value(game, depth)

def max_value(game, depth):
    #print("Running max_value...")
    best = -float('inf')
    actions = game.gen_actions()

    for action in actions[:SAMPLE]:
        new_game = game.clone()
        new_game.handle_action(action)

        best = max(best, value(new_game, depth - 1))

    return best

def chance_value(game, depth):
    #print("Running chance_value...")
    actions = game.gen_actions()

    if not actions:
        return heuristic(game)
    
    total = 0

    actions = actions[:SAMPLE]

    for action in actions:
        new_game = game.clone()
        new_game.handle_action(action)

        total += max_value(new_game, depth - 1)

    return total / len(actions)

def heuristic(game):
    #print("Running heuristic...")
    state = game.state

    progress = state.score / (state.required_score + 1)

    return (state.score + progress * 1000 + state.money * 10 + state.plays * 5)
