import math

class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self):
        self.visited_nodes = []
        self.pruned_branches = []

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player):
        self.visited_nodes.append(node.name)
        if depth == 0 or not node.children:
            node.minmax_value = node.value
            return node.value

        if maximizing_player:
            value = -math.inf
            for i, child in enumerate(node.children):
                value = max(value, self.alpha_beta_search(child, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    for sibling in node.children[i+1:]:
                        self.pruned_branches.append(sibling.name)
                    break 
            node.minmax_value = value
            return value
        else:
            value = math.inf
            for i, child in enumerate(node.children):
                value = min(value, self.alpha_beta_search(child, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    for sibling in node.children[i+1:]:
                        self.pruned_branches.append(sibling.name)
                    break
            node.minmax_value = value
            return value

# --- Tree setup ---
root = Node('Root')
n1, n2 = Node('N1'), Node('N2')
root.children = [n1, n2]

n3, n4, n5, n6 = Node('N3'), Node('N4'), Node('N5'), Node('N6')
n1.children, n2.children = [n3, n4], [n5, n6]

n3.children = [Node('L1', 4), Node('L2', 7)]
n4.children = [Node('L3', 2), Node('L4', 5)]
n5.children = [Node('L5', 1), Node('L6', 8)]
n6.children = [Node('L7', 3), Node('L8', 6)]

# --- Running the Simulation ---
agent = MinimaxAgent(depth=3)
env = Environment()
agent.act(root, env)


print("--- Minimax Values for All Visited Nodes ---")
for node_obj in [root, n1, n2, n3, n4, n5, n6]:
    print(f"Node {node_obj.name}: {node_obj.minmax_value}")

print("\n--- Pruning Info ---")
print(f"Nodes/Branches Pruned: {', '.join(env.pruned_branches) if env.pruned_branches else 'None'}")

print("\n--- Computation Comparison ---")
print(f"Nodes visited with Alpha-Beta: {len(env.visited_nodes)}")
print(f"Nodes visited with Standard Minimax: 15") 
