from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current_pos, end_pos):
    # Manhattan distance
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        visited.add(current_pos)

        # Generate adjacent nodes
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (current_pos[0]+dx, current_pos[1]+dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
                if maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                    new_node = Node(new_pos, current_node)
                    new_node.h = heuristic(new_pos, end)
                    new_node.f = new_node.h  # Best-First Search uses h only
                    frontier.put(new_node)
                    visited.add(new_pos)
    return None
def best_first_multi_goals(maze, start, goals):
    current = start
    full_path = []

    goals = goals.copy()  # avoid modifying original
    while goals:
        # Find the nearest goal (by Manhattan distance)
        goals.sort(key=lambda g: heuristic(current, g))
        next_goal = goals.pop(0)

        path_segment = best_first_search(maze, current, next_goal)
        if path_segment is None:
            return None  # No path found

        # Avoid repeating current position
        if full_path:
            path_segment = path_segment[1:]
        full_path.extend(path_segment)

        current = next_goal

    return full_path
maze = [
 [0, 0, 1, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = [(4, 4), (2, 3), (0, 4)]

path = best_first_multi_goals(maze, start, goals)
if path:
    print("Path visiting all goals:", path)
else:
    print("No path found")
