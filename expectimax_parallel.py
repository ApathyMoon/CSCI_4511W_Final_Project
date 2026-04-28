'''Single player Expectimax parellel thread algorithm for Balatro
Authors: Joshua Moellers'''
from simulation_worker import run_branch_task

def root_branch_eval(game, action_idx, depth, sample, executor=None):
    game = game.clone()
    game.handle_action_index(action_idx)
    if game.is_win:
        return 1e9, 1
    score, nodes = value(game, depth - 1, sample, executor)
    return score, nodes + 1

def fast_eval(game, idx):
    '''Prunes actions before feeding actions to the executor and going the searching the full depth'''
    try:
        temp_game = game.clone()
        temp_game.handle_action_index(idx)
    except Exception:
        return -1e9
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

def run_expectimax(game, depth=2, sample=8, pool=None):
    node_count = 0
    history_indices = []

    while not game.is_over:
        valid_indices = []
        action_mask = game.gen_action_space()
        for i, is_valid in enumerate(action_mask):
            if is_valid == 1:
                action = game.index_to_action(i)
                action_str = str(action)
                if "MoveCard" in action_str:
                    continue
                if "SelectCard" in action_str:
                    test = game.clone()
                    test.handle_action_index(i)
                    if len(test.state.selected) <= len(game.state.selected):
                        continue
                valid_indices.append(i)
                

        valid_indices.sort(key=lambda idx: fast_eval(game, idx), reverse=True)
        candidates = valid_indices if sample == -1 else valid_indices[:sample]

        if pool:
            tasks = []
            for idx in candidates:
                tasks.append(pool.apply_async(run_branch_task, (game, idx, depth, sample)))
            results = []
            for t in tasks:
                results.append(t.get())
            scores = [r[0] for r in results]
            node_count += sum(r[1] for r in results)
        else:
            scores = []
            for idx in candidates:
                s, n = root_branch_eval(game, idx, depth, sample)
                scores.append(s)
                node_count += n

        best_idx = candidates[scores.index(max(scores))]
        history_indices.append(best_idx)
        action_label = game.index_to_action(best_idx)
        game.handle_action_index(best_idx)
        print(f"action index played: {best_idx} | {action_label}")

    return game.state, game.is_win, node_count

def value(game, depth, sample, executor):
    if game.is_over or depth <= 0:
        return heuristic(game), 1
    
    return max_value(game, depth, sample, executor)

def max_value(game, depth, sample, executor):
    best = -float('inf')
    node_count = 1
    valid_indices = []
    action_mask = game.gen_action_space()

    for i, is_valid in enumerate(action_mask):
        if is_valid == 1:
            try:
                action = game.index_to_action(i)
                action_str = str(action)
                if "MoveCard" in action_str:
                    continue
                if "SelectCard" in action_str:
                    test = game.clone()
                    test.handle_action_index(i)
                    if len(test.state.selected) <= len(game.state.selected):
                        continue
                valid_indices.append(i)
            except Exception:
                pass

    valid_indices.sort(key=lambda idx: fast_eval(game, idx), reverse=True)

    if sample == -1:
        candidates = valid_indices
    elif depth > 1:
        candidates = valid_indices[:sample]
    else:
        candidates = valid_indices[:3]

    for idx in candidates:
        val, nodes = chance_value(game, idx, depth - 1, sample, executor)
        node_count += nodes
        best = max(best, val)

    return best, node_count

def chance_value(game, action_idx, depth, sample, executor):
    chance_sample_size = 8
    total = 0
    node_count = 1

    for _ in range(chance_sample_size):
        new_game = game.clone()
        new_game.handle_action_index(action_idx)
        score, nodes = value(new_game, depth, sample, executor)
        total += score
        node_count += nodes

    return (total / chance_sample_size), node_count

def heuristic(game):
    if game.is_over:
        return 1e9 if game.is_win else -1e9
    
    state = game.state
    score = state.score
    score += state.score / (state.required_score + 1) * 100
    score += state.plays * 100
    score += state.discards * 50
    score -= len(state.action_history) * 10
    
    return score
