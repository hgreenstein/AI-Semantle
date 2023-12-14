# AI Semantle: An AI Approach to Solving Semantle

## Introduction

AI Semantle is a sophisticated artificial intelligence project designed to tackle the popular word puzzle game, Semantle. In the wake of the Wordle phenomenon, games like Semantle have gained immense popularity, offering unique challenges that meld linguistic intuition with strategic gameplay. Semantle, in particular, sets itself apart by requiring players to guess a hidden word, receiving feedback in the form of similarity scores with each attempt. This project explores the application of AI techniques to effectively play and solve Semantle, leveraging advanced concepts in natural language processing and reinforcement learning.

### [Read the full report for even more detail](https://harrisgreenstein.com/assets/semantleReport-07e82c37.pdf)

## Project Overview

### High-Level Structure

AI Semantle is structured around a core AI agent capable of interacting with the Semantle game environment. This agent employs a combination of strategies and algorithms to emulate the decision-making process a human player might undertake. The project is divided into several key components:

- **Q-Learning Implementation**: At the heart of the AI Semantle agent is a Q-Learning algorithm. This machine learning approach enables the agent to make informed decisions based on the game's current state and learned experiences.
  
- **Clustering Mechanism**: To efficiently navigate the extensive vocabulary of Semantle, the AI employs clustering techniques. This approach groups semantically similar words, allowing the AI to make more strategic guesses.

- **Heuristic Functions**: The AI utilizes heuristic methods to choose specific words from clusters. These functions guide the agent towards more promising guesses based on the game's feedback.

- **Recurrent Neural Network (RNN) Integration**: An RNN model is incorporated to enhance the guessing strategy, especially in more complex scenarios where traditional methods may falter.

### AI Goals in Semantle

The primary objective of AI Semantle is to demonstrate the capability of an AI agent to reliably solve Semantle puzzles within a reasonable timeframe and with a high success rate. The project aims to showcase the effective application of AI algorithms in a game setting, providing insights into the potential of AI in natural language understanding and decision-making processes.

In the following sections, we will delve into the intricacies of the AI Semantle project, exploring each component's role and functionality in achieving this ambitious goal.



## Installation Guide

To get started with AI Semantle, follow these steps to set up the environment and install necessary dependencies. This guide assumes you have a basic understanding of Python environments and command-line operations.

### Prerequisites

Before installation, ensure you have the following prerequisites installed on your system:

- Python (version recommended: 3.8 or higher)
- `pip` for Python package management
- Git (optional, for cloning the repository)

### Setting Up the Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/hgreenstein/AI-Semantle.git
   cd AI-Semantle
   ```
2. **Install Dependencies**: AI Semantle relies on several Python libraries. These are listed in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

### Data Preparation:

AI Semantle requires the Google News dataset to function correctly. Follow these steps to set it up:

1. Download the Google News Dataset:
The dataset can be found at Kaggle. Download it to your local machine.
2. Configure the Dataset Path:
After downloading, specify the path to the dataset in the learning agent's configuration. Replace PATH_TO_DATASET in the code with the actual path where you saved the dataset.

### Running the AI Agent:

To test and evaluate the AI agent, follow these steps:

1. Initialize the Learning Agent:
Open qlearning.ipynb in Jupyter Notebook or JupyterLab.

2. Execute Initial Code Blocks:
Run the code blocks in qlearning.ipynb up to the one labeled "RUN THIS CODE BLOCK FOR TESTING WITH GREEDY HEURISTIC."

3. Testing the AI Agent:
Choose one of the following evaluation blocks to run, depending on the version of the AI you want to test:
- Greedy Heuristic
- RNN Approach
- Another specified approach

## AI Semantle: Component Overview and Results: 

The AI Semantle project integrates several complex components, each contributing to the AI's ability to solve the Semantle game. Here's an overview of these components and the results obtained from their implementation.

### Q-Learning
Q-Learning is a cornerstone of the AI Semantle project. It is a form of reinforcement learning that enables the AI to make decisions based on the game's current state and past experiences.

- **Functionality**: The AI uses Q-Learning to navigate through the game's environment, where actions are guesses, and states are defined by the game's feedback on these guesses.
- **Implementation Challenges**: The project team initially faced the "curse of dimensionality" due to the vast number of potential words. To tackle this, the state representation was simplified using binned similarity scores, significantly reducing the Q-table size.
- **Exploration vs Exploitation**: An epsilon-decay strategy was used to balance exploration (trying new words) and exploitation (using words with known high similarity scores).

### Clustering and Q-Agent Hierarchy
To manage the large action space (the set of all possible guesses), a hierarchical clustering approach was adopted.

- **Clustering Method**: Agglomerative hierarchical clustering was used for its effectiveness in grouping words based on semantic similarity.
- **Hierarchy of Q-Agents**: The AI comprises a primary Q-agent that selects a sub-agent, each responsible for a subset of word clusters. This hierarchical structure reduces the problem's complexity and improves decision-making efficiency.

### Heuristic Functions
Heuristic functions play a critical role in the AI's strategy by selecting the most promising words from the chosen clusters.

- **Greedy Approach**: The primary heuristic is a greedy algorithm that selects words based on the highest similarity scores from previous guesses.
- **RNN Approach**: As an alternative, a Recurrent Neural Network (RNN) model was experimented with to predict the similarity scores of potential guesses.

### Results and Evaluation
The project achieved notable results in terms of game-solving efficiency and speed.

- **Success Rate**: Using the greedy heuristic, the AI solved 79.2% of games within 50 guesses. The RNN approach had a lower success rate of 50.1%.
- **Guessing Speed**: The AI with the greedy heuristic guessed at an average of 0.002 seconds per guess, significantly faster than the RNN heuristic.
- **Exploration Efficiency**: The epsilon-decay approach proved effective, with the top Q-agent exploring nearly 600 out of 625 possible states in 10,000 games.

In summary, AI Semantle demonstrates a successful application of Q-Learning, clustering, and heuristic functions to solve the Semantle game efficiently. The project's results highlight the potential of AI in complex word puzzle environments, setting a benchmark for future developments in similar AI applications.
