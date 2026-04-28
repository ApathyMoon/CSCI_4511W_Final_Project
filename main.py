'''
Authors: Joshua Moellers
The code for Running the balatro simulations and also for testing the simulations
'''

'''
class Config(object)
     |  Static methods defined here:
     |
     |  __new__(*args, **kwargs)
     |      Create and return a new object.  See help(type) for accurate signature.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |                                                                                                                                                                                                                                                                                                                 
     |  ante_end                                                                                                                                                                                                                                                                                                       
     |                                                                                                                                                                                                                                                                                                                 
     |  available_max                                                                                                                                                                                                                                                                                                  
     |                                                                                                                                                                                                                                                                                                                 
     |  deck_max                                                                                                                                                                                                                                                                                                       
     |                                                                                                                                                                                                                                                                                                                 
     |  discarded_max                                                                                                                                                                                                                                                                                                  
     |                                                                                                                                                                                                                                                                                                                 
     |  discards                                                                                                                                                                                                                                                                                                       
     |                                                                                                                                                                                                                                                                                                                 
     |  joker_slots                                                                                                                                                                                                                                                                                                    
     |                                                                                                                                                                                                                                                                                                                 
     |  joker_slots_max                                                                                                                                                                                                                                                                                                
     |                                                                                                                                                                                                                                                                                                                 
     |  money_max                                                                                                                                                                                                                                                                                                      
     |                                                                                                                                                                                                                                                                                                                 
     |  plays                                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  selected_max                                                                                                                                                                                                                                                                                                   
     |                                                                                                                                                                                                                                                                                                                 
     |  stage_max                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                       
    class GameEngine(object)                                                                                                                                                                                                                                                                                           
     |  GameEngine(config=None)                                                                                                                                                                                                                                                                                        
     |                                                                                                                                                                                                                                                                                                                 
     |  Methods defined here:                                                                                                                                                                                                                                                                                          
     |
     |  clone() -> added by Joshua Moellers
     |                                                                                                                                                                                                                                                                                                                 
     |  gen_action_space(self, /)                                                                                                                                                                                                                                                                                      
     |                                                                                                                                                                                                                                                                                                                 
     |  gen_actions(self, /)                                                                                                                                                                                                                                                                                           
     |                                                                                                                                                                                                                                                                                                                 
     |  handle_action(self, /, action)                                                                                                                                                                                                                                                                                 
     |                                                                                                                                                                                                                                                                                                                 
     |  handle_action_index(self, /, index)                                                                                                                                                                                                                                                                            
     |                                                                                                                                                                                                                                                                                                                 
     |  ----------------------------------------------------------------------                                                                                                                                                                                                                                         
     |  Static methods defined here:                                                                                                                                                                                                                                                                                   
     |                                                                                                                                                                                                                                                                                                                 
     |  __new__(*args, **kwargs)                                                                                                                                                                                                                                                                                       
     |      Create and return a new object.  See help(type) for accurate signature.                                                                                                                                                                                                                                    
     |                                                                                                                                                                                                                                                                                                                 
     |  ----------------------------------------------------------------------                                                                                                                                                                                                                                         
     |  Data descriptors defined here:                                                                                                                                                                                                                                                                                 
     |                                                                                                                                                                                                                                                                                                                 
     |  is_over                                                                                                                                                                                                                                                                                                        
     |                                                                                                                                                                                                                                                                                                                 
     |  is_win                                                                                                                                                                                                                                                                                                         
     |                                                                                                                                                                                                                                                                                                                 
     |  state                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                       
    class GameState(object)                                                                                                                                                                                                                                                                                            
     |  Methods defined here:                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  __repr__(self, /)                                                                                                                                                                                                                                                                                              
     |      Return repr(self).                                                                                                                                                                                                                                                                                         
     |                                                                                                                                                                                                                                                                                                                 
     |  ----------------------------------------------------------------------                                                                                                                                                                                                                                         
     |  Static methods defined here:                                                                                                                                                                                                                                                                                   
     |                                                                                                                                                                                                                                                                                                                 
     |  __new__(*args, **kwargs)                                                                                                                                                                                                                                                                                       
     |      Create and return a new object.  See help(type) for accurate signature.                                                                                                                                                                                                                                    
     |                                                                                                                                                                                                                                                                                                                 
     |  ----------------------------------------------------------------------                                                                                                                                                                                                                                         
     |  Data descriptors defined here:                                                                                                                                                                                                                                                                                 
     |                                                                                                                                                                                                                                                                                                                 
     |  action_history                                                                                                                                                                                                                                                                                                 
     |                                                                                                                                                                                                                                                                                                                 
     |  available                                                                                                                                                                                                                                                                                                      
     |                                                                                                                                                                                                                                                                                                                 
     |  deck                                                                                                                                                                                                                                                                                                           
     |                                                                                                                                                                                                                                                                                                                 
     |  discarded                                                                                                                                                                                                                                                                                                      
     |                                                                                                                                                                                                                                                                                                                 
     |  discards                                                                                                                                                                                                                                                                                                       
     |                                                                                                                                                                                                                                                                                                                 
     |  jokers                                                                                                                                                                                                                                                                                                         
     |                                                                                                                                                                                                                                                                                                                 
     |  money                                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  plays                                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  required_score                                                                                                                                                                                                                                                                                                 
     |                                                                                                                                                                                                                                                                                                                 
     |  round                                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  score                                                                                                                                                                                                                                                                                                          
     |                                                                                                                                                                                                                                                                                                                 
     |  selected                                                                                                                                                                                                                                                                                                       
     |                                                                                                                                                                                                                                                                                                                 
     |  stage                                                                                                                                                                                                                                                                                                          
                                                                                                                                                                                                                                                                                                                       
    class Stage(object) -> Not important
'''

import pylatro
import expectimax
import time
import csv
import multiprocessing

def expectimax_worker_task(task_id):
    game = pylatro.GameEngine()
    start = time.perf_counter()
    state, win, nodes = expectimax.run_expectimax(game, depth=5, sample=16)
    end = time.perf_counter()
    runtime = end - start
    num_plays = 0
    num_discards = 0
    for action in state.action_history:
        if "Play" in str(action):
            num_plays += 1
        if "Discard" in str(action):
            num_discards += 1
    print(f"Game {task_id} finished")
    return task_id, state.score, state.round, num_plays, num_discards, len(state.action_history), nodes, round(runtime, 4), win

def run_and_record_expectimax(n=100):
    header = ['id,', 'score', 'round', 'plays', 'discards', 'action_history_length', 'nodes_expanded', 'runtime', 'win']
    num_threads = 32

    with multiprocessing.Pool(processes=num_threads) as pool:
        results = pool.map(expectimax_worker_task, range(n))

        with open('expectimax_results.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)

            for (id, score, round, plays, discards, action_len, nodes, runtime, win) in results:
                writer.writerow([
                    id,
                    score, 
                    round, 
                    plays, 
                    discards, 
                    action_len, 
                    nodes, 
                    runtime,
                    win])

if __name__ == "__main__":
    # config = pylatro.Config()
    # config.ante_end = 1
    # run_expectimax_once(
    #     expectimax_parallel.run_expectimax, 
    #     config=config, 
    #     depth=3, 
    #     sample=8, 
    #     timing=True, 
    #     printing="Parallel Expectimax")

    run_and_record_expectimax(n=100)
