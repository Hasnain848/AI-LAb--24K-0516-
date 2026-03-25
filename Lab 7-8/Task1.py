import math

class Node:
    def __init__(self, value=None):
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
            return environment.compute_minimax(node, self.depth)
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.minmax_value if node.minmax_value is not None else node.value
 

        if maximizing_player:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)
            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)


root = Node('root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]

n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n1.children = [n3, n4]
n2.children = [n5, n6]

n7 = Node(4)
n8 = Node(7)
n9 = Node(2)
n10 = Node(5)
n3.children = [n7, n8]
n4.children = [n9, n10]

n11 = Node(1)
n12 = Node(8)
n13 = Node(3)
n14 = Node(6)
n5.children = [n11, n12]
n6.children = [n13, n14]

depth = 3

agent = MinimaxAgent(depth)
environment = Environment(root)

run_agent(agent, environment, root)

print("Computed Nodes:", environment.computed_nodes)


print("Minimax values:")
print("ROOT:", root.minmax_value)
print("N1:", n1.minmax_value)
print("N2:", n2.minmax_value)
print("N3:", n3.minmax_value)
print("N4:", n4.minmax_value)
print("N5:", n5.minmax_value)
print("N6:", n6.minmax_value)

print("Updated min max values:")
depth=2
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)
print("Minimax values:")
print("ROOT:", root.minmax_value)
print("N1:", n1.minmax_value)
print("N2:", n2.minmax_value)
#print("N3:", n3.minmax_value)
#print("N4:", n4.minmax_value)
#print("N5:", n5.minmax_value)
#print("N6:", n6.minmax_value)
