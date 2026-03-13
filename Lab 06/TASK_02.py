def beam_search(start=1, goal=20, k=2):
    def h(n): return abs(goal - n)
    beam = [(h(start), start, [start])]
    level = 0
    while beam:
        print(f"Level {level} explored: {[node[1] for node in beam]}")
        candidates = []
        for _, current, path in beam:
            if current == goal:
                return path
            successors = [current + 2, current + 3, current * 2]
            for s in successors:
                candidates.append((h(s), s, path + [s]))
        candidates.sort(key=lambda x: x[0])
        beam = candidates[:k]
        level += 1
    
    return None

final_path = beam_search()
print(f"Final path to reach 20: {final_path}")
