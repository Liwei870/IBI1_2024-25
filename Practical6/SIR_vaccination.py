import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
# Input the parameters
#Write the formula that how to calculate the Susceptible individuals
# Write the formula that howw to calculate the new S,I,R in the time loop
# plot the picture
# Model parameters
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
N = 10000  # Total population size
t_max = 1000  # Maximum number of time step
vaccination_rate = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
for rate in vaccination_rate:
    S = (1-rate)*N-1# Susceptible individuals, minus one initial infected
    I = 1# Initial infected individuals
    R = 0 # Recovered individuals
    V = N*rate
    S_list= [S]#S: Susceptible individuals
    I_list = [I]#I: Infected individuals
    R_list= [R]# R: Recovered individuals
#Calculate the Susceptible , Infected , recovered individuals in loop
    for t in range(t_max):
        S = S -S*beta*I/N
        I = I + S*beta*I/N - gamma*I
        R = R + I* gamma
    # Update the number of individuals in each compartment
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
 # Plot the number of infected individuals for different vaccination rates
    plt.plot(range(t_max + 1), I_list, label=f"{rate * 100}%", color=cm.viridis(int(rate * 400)))
plt.title('SIR model with different vaccination rates')
plt.xlabel('time')
plt.ylabel('number of people')
plt.legend()
plt.show()



    
  
