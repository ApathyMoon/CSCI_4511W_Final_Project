'''MCTS algorithm for Balatro
Author: Joshua Moellers'''
import math
import random

class MCTSNode:
    def __init__(self, game, parent=None, action=None):
        self.game = game
        self.parent = parent
        self.action = action
        self.children = {}
        self.wins = 0
        self.rollouts = 0
        self.untried_actions = [a for a in game.gen_actions() if "MoveCard" not in str(a)]
        # self.untried_actions = game.gen_actions()

    def select(self):
        current = self
        while not current.untried_actions and current.children:
            current = current.ucb_select()
        return current
    
    def expand(self):
        if self.game.is_over or not self.untried_actions:
            return self
        
        action = self.untried_actions.pop()
        new_game = self.game.clone()
        new_game.handle_action(action)

        child_node = MCTSNode(new_game, parent=self, action=action)
        self.children[str(action)] = child_node
        return child_node

    def ucb_select(self, c=1.41):
        best_score = -float('inf')
        best_child = None
        for child_node in self.children.values():
            if child_node.rollouts == 0: return child_node
            score = (child_node.wins / child_node.rollouts) + c * math.sqrt(math.log(self.rollouts) / child_node.rollouts)
            if score > best_score:
                best_score = score
                best_child = child_node
        return best_child
    
def mcts_search(root_game, iterations=1000):
    root = MCTSNode(game=root_game.clone())

    for _ in range(iterations):
        leaf = root.select()
        child = leaf.expand()
        result = rollout(child.game)
        back_propagate(result, child)

    if not root.children:
        return root.untried_actions[0] if root.untried_actions else None
    best_child_node = max(root.children.values(), key=lambda node: node.rollouts)
    return best_child_node.action

def heuristic(game, root_game):
    if game.is_win: return 10.0
    if game.state.round > root_game.state.round: return 2.0

    state = game.state
    score = (state.score / (state.required_score + 1)) / (10 ** len(str(abs(root_game.state.score))))

    return score
    
def rollout(game):
    temp_game = game.clone()
    while not temp_game.is_over:
        actions = [a for a in temp_game.gen_actions() if "MoveCard" not in str(a)]
        # actions = temp_game.gen_actions()
        if not actions: break
        action = random.choice(actions)
        temp_game.handle_action(action)
    return heuristic(temp_game, game)

def back_propagate(result, node):
    while node is not None:
        node.rollouts += 1
        node.wins += result
        node = node.parent
