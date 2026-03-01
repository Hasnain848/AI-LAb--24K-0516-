# Graph with different edge costs
graph = {
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {},
}

heuristic = {
    'A': 14, 'B': 12, 'C': 11,
    'D': 6, 'E': 4, 'F': 11, 'G': 0
}


def a_star(graph, start, goal):
    frontier = [(start, heuristic[start])]
    visited = set()
    g_costs = {start: 0}
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])  # Sort by f(n)
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print("Optimal Path:", path)
            return path

        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristic[neighbor]
                frontier.append((neighbor, f_cost))
                came_from[neighbor] = current_node

    print("Goal not found")
    return None

def update_edge(graph, node1, node2, new_cost):
    if node2 in graph[node1]:
        graph[node1][node2] = new_cost
        print(f"\nEdge cost updated: {node1} -> {node2} = {new_cost}")
    else:
        print("Edge does not exist!")

# Initial Run
print("Initial A* Search:")
a_star(graph, 'A', 'G')
# Dynamic Change Example 1
update_edge(graph, 'A', 'B', 8)

print("\nRecomputing after change...")
a_star(graph, 'A', 'G')
# Dynamic Change Example 2
update_edge(graph, 'B', 'E', 7)

print("\nRecomputing after change...")
a_star(graph, 'A', 'G')
