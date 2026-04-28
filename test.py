import pylatro
import pickle

game = pylatro.GameEngine()
try:
    data = pickle.dumps(game)
    print("Pickle successful!")
    new_game = pickle.loads(data)
    print("Unpickle successful!")
except Exception as e:
    print(f"Pickle failed: {e}")
