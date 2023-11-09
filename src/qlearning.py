import numpy as np
import bisect 
import math
import random 
import gensim
from answers import secretWords as answers
from constants import PATH_TO_DATASET

gnews_model = gensim.models.KeyedVectors.load_word2vec_format(PATH_TO_DATASET, binary=True)

class environment:
    def __init__(self, mystery_word, clusters):
        self.mystery_word = mystery_word
        self.clusters = clusters
        self.guessed_words = []
        self.state = []
        for i in range(len(clusters)): self.state.append(0); 
    
    def binSimilarityScore(self, similarityScore):
        bins = [0, 5, 15, 25]
        return bisect.bisect_left(bins, similarityScore)
    
    def guess_word(self, word, clusterNumber):
        if(word == self.mystery_word):
            return 100
        similarity_score = round(100 * gnews_model.similarity(word, self.mystery_word), 6)
        self.guessed_words.append((word, similarity_score))
        self.guessed_words = sorted(self.guessed_words, key=lambda x: x[1], reverse = True)
        binned_score = self.binSimilarityScore(similarity_score)
        #if(binned_score > self.state[clusterNumber]):
        self.state[clusterNumber] = binned_score
        return similarity_score


    def get_state(self):
        return self.state

class QAgent():
    def __init__(self, num_clusters, num_bins, learning_rate, discount_rate, epsilon_decay):
        self.num_clusters = num_clusters
        self.num_bins = num_bins
        self.learning_rate = learning_rate
        self.discount_rate = discount_rate
        self.epsilon = 1.0 
        self.epsilon_decay = epsilon_decay
        self.q_table = {}
        for a in range(num_bins):
            for b in range(num_bins):
                for c in range(num_bins):
                    for d in range(num_bins):
                        tempState = (a, b, c, d)
                        self.q_table[tempState] = [0] * num_clusters

    def choose_action(self, state):
        if random.random() < self.epsilon:
            action = random.randint(0, self.num_clusters - 1)
        #print("Picking action", action)
            return action 
        else:
            return np.argmax(self.q_table[state])
    
    def update(self, state, action, reward, next_state):
        #print("Updating ", state, action)
        current_q = self.q_table[state][action]
        max_next_q = np.max(self.q_table[next_state])
        new_q = current_q + self.learning_rate * (reward + self.discount_rate * max_next_q - current_q)
        self.q_table[state][action] = new_q
    
    def decayEpsilon(self, game_number):
        self.epsilon = 0.01 + (1.0 - 0.01) * math.exp(-self.epsilon_decay * game_number)

def choose_word_from_cluster(cluster, guessed_words, similarity_threshold=20):
    if not guessed_words:
        return cluster[random.randint(0, len(cluster) - 1)]

    best_word = guessed_words[0][0]
    worst_word = guessed_words[-1][0]
    best_similarity = guessed_words[0][1]

    # Get word vectors for words in the cluster
    cluster_vectors = np.array([gnews_model[word] for word in cluster])

    # Calculate similarity to the best and worst words
    best_word_vec = gnews_model[best_word]
    worst_word_vec = gnews_model[worst_word]

    similarity_to_best = np.dot(cluster_vectors, best_word_vec) / (np.linalg.norm(cluster_vectors, axis=1) * np.linalg.norm(best_word_vec))
    similarity_to_worst = np.dot(cluster_vectors, worst_word_vec) / (np.linalg.norm(cluster_vectors, axis=1) * np.linalg.norm(worst_word_vec))

    if best_similarity < similarity_threshold:
        adjusted_similarity = (similarity_to_best + similarity_to_worst) / 2
    else:
        adjusted_similarity = similarity_to_best - similarity_to_worst

    # Get the index of the word with the highest adjusted similarity
    best_index = np.argmax(adjusted_similarity)

    return cluster[best_index]


mystery_word = answers[random.randint(0, len(answers) - 1)]
from clusters import clusters 
num_clusters = len(clusters)
num_bins = 5
learning_rate = 0.3
discount_rate = 0.75
epsilon_decay = 0.04

env = environment(mystery_word, clusters)
q_agent = QAgent(num_clusters, num_bins, learning_rate, discount_rate, epsilon_decay)
num_games = 20000
max_guesses = 50
similarity_score = 0 

for num_game in range(num_games):
    state = tuple(env.get_state())
    for i in range(max_guesses):
        if(similarity_score != 100):
            action = q_agent.choose_action(state)
            word = choose_word_from_cluster(env.clusters[action], env.guessed_words)
            similarity_score = env.guess_word(word, action)
            next_state = tuple(env.get_state())
            q_agent.update(state, action, similarity_score, next_state)
            state = next_state
        else:
            print("Solved game ", num_game, " in ", i)
            similarity_score = 0 
            break 
    env.guessed_words = []
    mystery_word = answers[random.randint(0, len(answers) - 1)]
    q_agent.decayEpsilon(num_game)
for state, actions in q_agent.q_table.items():
    nonzero_actions = [action_value for action_value in actions if action_value != 0]
    #if nonzero_actions:
        #print(f"Label: {state}, Learning: {actions}")


        

