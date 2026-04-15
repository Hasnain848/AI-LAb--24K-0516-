import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]
transition_matrix = np.array([
    [0.7, 0.2, 0.1],  # From Sunny
    [0.3, 0.4, 0.3],  # From Cloudy
    [0.2, 0.3, 0.5]   # From Rainy
])

def simulate_weather(num_days=10, start_state=0):
    current_state = start_state
    sequence = [states[current_state]]

    rainy_count = 1 if states[current_state] == "Rainy" else 0

    for _ in range(num_days - 1):
        current_state = np.random.choice(
            [0, 1, 2], p=transition_matrix[current_state]
        )
        sequence.append(states[current_state])
        if states[current_state] == "Rainy":
            rainy_count += 1

    return sequence, rainy_count

np.random.seed(42)
sequence, count = simulate_weather(10)
print("Sample 10-day forecast:", " → ".join(sequence))
print(f"Rainy days in sample: {count}\n")

trials = 10000
at_least_3_rainy = sum(
    1 for _ in range(trials) if simulate_weather(10)[1] >= 3
)

print(f"Trials run         : {trials}")
print(f"P(≥3 rainy days)   : {at_least_3_rainy / trials:.4f}")
