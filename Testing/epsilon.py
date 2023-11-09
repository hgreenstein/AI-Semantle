import math
import matplotlib.pyplot as plt
import random

def plot_exploration_vs_exploitation(epsilon_decay, num_games):
    epsilons = []
    explorations = []
    exploitations = []

    for i in range(num_games):
        epsilon = 0.01 + (1.0 - 0.01) * math.exp(-epsilon_decay * i)
        epsilons.append(epsilon)

        exploration_count = 0
        exploitation_count = 0
        for j in range(1000): # simulate 1000 actions at each game number to compute exploration vs exploitation ratio
            if random.random() < epsilon:
                exploration_count += 1
            else:
                exploitation_count += 1
        exploration_ratio = exploration_count / 1000
        exploitation_ratio = exploitation_count / 1000
        explorations.append(exploration_ratio)
        exploitations.append(exploitation_ratio)

    fig, ax = plt.subplots()
    ax.plot(range(num_games), explorations, label='Exploration')
    ax.plot(range(num_games), exploitations, label='Exploitation')
    ax.legend()
    ax.set_title('Exploration vs Exploitation over Time')
    ax.set_xlabel('Game Number')
    ax.set_ylabel('Ratio')
    plt.show()
plot_exploration_vs_exploitation(0.001, 20000)