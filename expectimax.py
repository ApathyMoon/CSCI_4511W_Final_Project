'''Single player Expectimax algorithm for Balatro
Authors: Joshua Moellers'''

node_count = 0

def fast_eval(game, a):
    '''Prunes actions before feeding actions to the executor and going the searching the full depth'''
    temp_game = game.clone()
    temp_game.handle_action(a)
    state = temp_game.state

    if temp_game.is_win: return 1e9
    if temp_game.is_over: return -1e9

    score = state.score * 10
    score += state.score / (state.required_score + 1) * 500
    score += state.plays * 50
    score += state.discards * 25
    score += len(state.selected) * 5
    score += len(state.available) * 2

    return score

def run_expectimax(game, depth=2, sample=10):
    global node_count
    node_count = 0
    while not game.is_over:
        actions = game.gen_actions()
        actions = [a for a in actions if "MoveCard" not in str(a)]
        # actions.sort(key=lambda a: fast_eval(game, a), reverse=True)
        actions = actions if sample == -1 else actions[:sample]

        best_score = -float('inf')
        best_action = actions[0]

        for action in actions:
            new_game = game.clone()
            new_game.handle_action(action)

            score = value(new_game, depth, sample)

            if score > best_score:
                best_score = score
                best_action = action
        
        print("action:", best_action)
        game.handle_action(best_action)

    return game.state, game.is_win, node_count

def value(game, depth, sample):
    global node_count
    node_count += 1
    if game.is_over or depth <= 0:
        return heuristic(game)
    
    return max_value(game, depth, sample)

def max_value(game, depth, sample):
    global node_count
    node_count += 1
    best = -float('inf')
    actions = game.gen_actions()
    actions = [a for a in actions if "MoveCard" not in str(a)]
    # actions.sort(key=lambda a: fast_eval(game, a), reverse=True)
    actions = actions if sample == -1 else actions[:sample]

    for action in actions:
        val = chance_value(game, action, depth - 1, sample)
        best = max(best, val)

    return best

def chance_value(game, action, depth, sample):
    global node_count
    node_count += 1
    chance_sample_size = 8
    total = 0

    for _ in range(chance_sample_size):
        new_game = game.clone()
        new_game.handle_action(action)
        total += value(new_game, depth, sample)

    return total / chance_sample_size

def heuristic(game):
    # Terminal state
    if game.is_over:
        return 1e9 if game.is_win else -1e9
    
    state = game.state
    score = state.score * 250
    score += (state.score / (state.required_score + 1)) * 500
    score += state.plays * 50
    score += state.discards * 25
    score += len(state.selected) * 20
    score += len(state.available) * 10
    score -= len(state.action_history) * 5

    return score
