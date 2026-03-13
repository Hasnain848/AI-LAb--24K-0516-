import random
def genetic_algorithm():
    pop_size = 10
    generations = 15
    mutation_rate = 0.1
    def decode(binary_str): return int(binary_str, 2)
    def fitness(x): return x**2 + 2*x

    population = [''.join(random.choice('01') for _ in range(5)) for _ in range(pop_size)]
    for gen in range(generations):
        pop_fitness = [(chrom, fitness(decode(chrom))) for chrom in population]
        
        # Selection
        pop_fitness.sort(key=lambda x: x[1], reverse=True)
        parents = [x[0] for x in pop_fitness[:pop_size//2]]

        new_population = []
        while len(new_population) < pop_size:
            # Crossover
            p1, p2 = random.sample(parents, 2)
            point = random.randint(1, 4)
            child = p1[:point] + p2[point:]
            
            # Mutation 
            if random.random() < mutation_rate:
                idx = random.randint(0, 4)
                bit_list = list(child)
                bit_list[idx] = '1' if bit_list[idx] == '0' else '0'
                child = ''.join(bit_list)
            
            new_population.append(child)
        
        population = new_population
    best_chrom = max(population, key=lambda c: fitness(decode(c)))
    best_x = decode(best_chrom)
    print(f"Best chromosome: {best_chrom}")
    print(f"Best value of x: {best_x}")
    print(f"Best fitness value: {fitness(best_x)}")

genetic_algorithm()
