def f(x):
    return -x**2 + 6*x

def hill_climbing():
    import random
    current_x = random.randint(0, 6)
    print(f"Initial value of x: {current_x}")
    while True:
        current_f = f(current_x)
        print(f"Current x: {current_x}, f(x): {current_f}")
        neighbors = []
        if current_x + 1 <= 6: neighbors.append(current_x + 1)
        if current_x - 1 >= 0: neighbors.append(current_x - 1)
        best_neighbor = None
        best_f = current_f
        for neighbor in neighbors:
            if f(neighbor) > best_f:
                best_f = f(neighbor)
                best_neighbor = neighbor
        if best_neighbor is None:
            return current_x, current_f
        current_x = best_neighbor
final_x, final_f = hill_climbing()
print(f"Final optimal value: x = {final_x}, f(x) = {final_f}")
