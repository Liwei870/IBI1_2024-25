#Pseudocode:
#Import necessary libraries
#Model the spatial SIR model using a grid-based approach
#Create a 100x100 grid to represent the population
#Randomly select an initial infected individual
#Lists to record the number of individuals in each state at each time step
#Count the number of individuals in each state at the current time step
#Update the number of individuals in each state based on the infection and recovery processes
# Plot the heatmap of the population state at specific time points
import numpy as np
import matplotlib.pyplot as plt
# Model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
t_max = 100
#Create a 100x100 array representing all susceptible individuals
population = np. zeros( (100, 100) )
# Randomly select an initial infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
# Lists to record the number of individuals in each state at each time step
susceptible_counts = []
infected_counts = []
recovered_counts = []

# Simulation process
for t in range(t_max):
    # Count the number of individuals in each state at the current time step
    s_count = np.sum(population == 0)
    i_count = np.sum(population == 1)
    r_count = np.sum(population == 2)

    susceptible_counts.append(s_count)
    infected_counts.append(i_count)
    recovered_counts.append(r_count)

    # Find the coordinates of all infected individuals
    infected_indices = np.argwhere(population == 1)

    for idx in infected_indices:
        x, y = idx[0], idx[1]

        # Iterate through the 8 neighbors of the infected individual
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                new_x, new_y = x + dx, y + dy

                # Check if the neighbor is within the range and is a susceptible individual
                if 0 <= new_x < 100 and 0 <= new_y < 100 and population[new_x, new_y] == 0:
                    if np.random.random() < beta:
                        population[new_x, new_y] = 1

        # The infected individual recovers with a probability of gamma
        if np.random.random() < gamma:
            population[x, y] = 2

    # Only plot the heatmap at time points 0, 10, 50, and 100
    if t in [0, 10, 50, 99]:
        plt.figure( figsize =(6,4),dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Population State at Time Step {t}")
        plt.xlabel("Column")
        plt.ylabel("Row")
        plt.colorbar(label="State (0: Susceptible, 1: Infected, 2: Recovered)")
        plt.show()