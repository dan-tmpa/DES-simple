import numpy as np
from math import log
from random import random
import matplotlib.pyplot as plt

# Defining global variables
mission_time = 5*24*365  # Mission time. Unit: h.
n = 100000  # Number of simulation runs.

# Utility functions for calculations
def weibull_inverse_cdf(p, shape, scale):
    """
    Calculate the inverse CDF of the Weibull distribution with shape 'shape' and scale 'scale'
    evaluated at p.
    """
    return scale * (-log(1-p))**(1/shape)

def exponential_inverse_cdf(p, rate):
    """
    Calculate the inverse CDF of the exponential distribution with rate 'rate'
    evaluated at p.
    """
    return -log(1-p) / rate

# Parameters of the time-to-failure probability distribution (Weibull)
shape = 1.5  # Shape parameter. Unitless.
scale = 2000  # Scale parameter. Unit: h.

# Parameters of the repair time probability distribution (Exponential)
repair_rate = 4E-03  # Repair rate. Unit: 1/h.

# Simulation

# Creating a time vector
k = 300  # Size of the time vector. Unitless.
t = np.linspace(0, mission_time, k)  # Time vector. Unit: hours.

# Matrices to store results
# Convention: 0 -> system available; 1 -> system unavailable.
s = np.zeros((n, k), dtype=np.int8)  # Matrix of states over time for each simulation run.

# Main simulation loop
for i in range(n):
    current_state = 0  # Current system state in a simulation run.
    t_sim = 0  # Elapsed time in the simulation. Unit: hours.

    # Loop for the current simulation run.
    while t_sim <= mission_time:
        if current_state == 0:
            p = random()  # Pseudo-random number between 0 and 1.
            t_trans = t_sim + weibull_inverse_cdf(p, shape, scale)  # Failure transition time. Unit: hours.
            s[i, (t > t_sim) & (t <= t_trans)] = 0
            t_sim = t_trans
            current_state = 1

        else:  # current_state == 1
            p = random()  # Pseudo-random number between 0 and 1.
            t_trans = t_sim + exponential_inverse_cdf(p, repair_rate)  # Repair transition time. Unit: hours.
            s[i, (t > t_sim) & (t <= t_trans)] = 1
            t_sim = t_trans
            current_state = 0

# Calculating estimators
unavailability_1k = np.sum(s[0:1000, :], axis=0) / 1000
unavailability_10k = np.sum(s[0:10000, :], axis=0) / 10000
unavailability_100k = np.sum(s[0:100000, :], axis=0) / 100000

# Plot 1: only 1k
plt.figure()
plt.plot(t / (365*24), unavailability_1k, label='1,000 runs')
plt.xlabel('Time (years)')
plt.ylabel('Unavailability')
plt.ylim(0, 0.20)
plt.grid(True)
plt.legend()
plt.title('Unavailability - 1,000 runs')
plt.show()

# Plot 2: 1k and 10k
plt.figure()
plt.plot(t / (365*24), unavailability_1k, label='1,000 runs')
plt.plot(t / (365*24), unavailability_10k, label='10,000 runs')
plt.xlabel('Time (years)')
plt.ylabel('Unavailability')
plt.ylim(0, 0.20)
plt.grid(True)
plt.legend()
plt.title('Unavailability - 1,000 and 10,000 runs')
plt.show()

# Plot 3: 1k, 10k and 100k
plt.figure()
plt.plot(t / (365*24), unavailability_1k, label='1,000 runs')
plt.plot(t / (365*24), unavailability_10k, label='10,000 runs')
plt.plot(t / (365*24), unavailability_100k, label='100,000 runs')
plt.xlabel('Time (years)')
plt.ylabel('Unavailability')
plt.ylim(0, 0.20)
plt.grid(True)
plt.legend()
plt.title('Unavailability - 1,000, 10,000 and 100,000 runs')
plt.show()