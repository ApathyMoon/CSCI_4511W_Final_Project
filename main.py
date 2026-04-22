'''
Authors: Jeffery Gothmann, Daniel Hernandez, Joshua Moellers
The code for Running the balatro simulations and also for testing the simulations
'''
import pylatro

if __name__ == "__main__":
    game = pylatro.GameEngine()

    current_state = game.state
    
    print(current_state)
'''
    while not game.is_over:
        pass
'''
