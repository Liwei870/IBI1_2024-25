#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Define the SIR model
# S: Susceptible individuals
# I: Infected individuals
# R: Recovered individuals
# beta: Infection rate
# gamma: Recovery rate
# N: Total population
# t: Time period
# Return: Plot the SIR model
def SIR_model(S, I, R, beta, gamma, N):
    S = [S]
    I = [I]
    R = [R]
    t = 1000
# Loop through the time period
# Calculate the new number of susceptible, infected, and recovered individuals
# Append the new values to the lists
    for i in range(t):
        new_S = S[-1] - beta * S[-1] * I[-1] / N
        new_I = I[-1] + beta * S[-1] * I[-1] / N - gamma * I[-1]
        new_R = R[-1] + gamma * I[-1]
        S.append(new_S)
        I.append(new_I)
        R.append(new_R)
# Plot the SIR model
    plt.figure(figsize=(6, 4), dpi=150)
    plt.plot(S, label='Susceptible')
    plt.plot(I, label='Infected')
    plt.plot(R, label='Recovered')
    plt.xlabel('Time')
    plt.ylabel('Number of individuals')
    plt.title('SIR model')
    plt.legend()
    plt.show()
    plt.savefig("SIR_model.png")
# Call the SIR model function
# Set the initial values for the number of susceptible, infected, recovered individuals, infection rate, recovery rate, and total population
# Pseudocode: Assume the initial values are S=9999, I=1, R=0, beta=0.3, gamma=0.05, N=10000
SIR_model(9999, 1, 0, 0.3, 0.05, 10000)

    

    
   
    
