'''helper module for implementing multiprocessing to make expectimax and mcts faster
Author: Joshua Moellers'''

import pylatro
import expectimax_parallel

engine = None

def init_worker():
    global engine
    engine = pylatro.GameEngine()

def run_branch_task(sim_game, action_idx, depth, sample):
    return expectimax_parallel.root_branch_eval(sim_game, action_idx, depth, sample)
