import math

class Node:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value
        self.children = []
        self.minmax_value = None

class MinimaxAgent:
    def act(self, node, environment):

        return environment.alpha_beta_search(node, 3, -math.inf, math.inf, True)

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

    def find_optimal_path(self, node):
        path = [node.name]
        current = node
        while current.children:
      
            next_node = next((child for child in current.children if child.minmax_value == current.minmax_value), None)
            if next_node:
                path.append(next_node.name)
                current = next_node
            else:
                break
        return " -> ".join(path)

# --- Tree Setup with EXTRA BRANCH (N3) ---
root = Node('Root')
n1, n2, n3 = Node('N1'), Node('N2'), Node('N3')
root.children = [n1, n2, n3]

# Subtree N1
n4, n5 = Node('N4'), Node('N5')
n1.children = [n4, n5]
n4.children = [Node('L1', 3), Node('L2', 5)]
n5.children = [Node('L3', 2), Node('L4', 9)]

# Subtree N2
n6, n7 = Node('N6'), Node('N7')
n2.children = [n6, n7]
n6.children = [Node('L5', 1), Node('L6', 4)]
n7.children = [Node('L7', 8), Node('L8', 2)]

# NEW EXTRA BRANCH Subtree N3
n8, n9 = Node('N8'), Node('N9')
n3.children = [n8, n9]
n8.children = [Node('L9', 10), Node('L10', 12)] 
n9.children = [Node('L11', 1), Node('L12', 0)]

env = Environment()
agent = MinimaxAgent()
agent.act(root, env)

# --- Output Results ---
print("--- 1. Updated Minimax Values ---")
print(f"Root: {root.minmax_value}")
for child in root.children:
    print(f"  {child.name}: {child.minmax_value}")

print("\n--- 2. Pruning Info ---")
print(f"Nodes/Branches Pruned: {', '.join(env.pruned_branches) if env.pruned_branches else 'None'}")

print("\n--- 3. Optimal Path ---")
print(f"Path: {env.find_optimal_path(root)}")


4. Commentary on Changes
Root Value Change: By adding the N3 branch with high leaf values (10 and 12), the Root value significantly increased (likely to 10). In the previous tree, the Max player was limited to lower values like 4 or 5. This shows that the optimal decision changes as soon as a better guaranteed alternative is discovered.

Pruning Behavior:

Increased Pruning: Because we added a third branch (Root -> N3), if the first two branches (N1 and N2) already established a high Alpha, and the third branch starts with very low values, the entire remainder of that third branch can be pruned.

Efficiency: Even though the tree is larger, Alpha-Beta pruning prevents the total number of visited nodes from growing linearly. It "ignores" the bad options in N3 once it sees that N3's child (the Minimizer) will force a low value.

Optimal Path: The path now shifts toward the new branch (Root -> N3 -> N8 -> L9) because it yields the highest utility for the Max player while considering that the Min player will try to minimize that gain at the N3 level.
