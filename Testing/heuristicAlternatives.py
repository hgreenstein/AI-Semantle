def sigmoid(x, max_value=70, min_value=0, k=0.1):
    return 1 / (1 + math.exp(-k * (x - (min_value + (max_value - min_value) / 2))))

def choose_word_from_cluster(cluster, past_guesses):
    scores = []

    for word in cluster:
        word_score = 0

        for past_word, similarity in past_guesses:
            # Calculate the weight for each past guess using the sigmoid function
            weight = sigmoid(similarity)

            # Calculate similarity with the current word in the cluster
            word_similarity = gnews_model.similarity(word, past_word)

            # Update the word_score considering the weight and word similarity
            word_score += weight * word_similarity

        scores.append((word, word_score))

    # Select the word with the highest score
    best_word, _ = max(scores, key=lambda x: x[1])
    return best_word
def similarity_matrix(past_guesses_matrix, cluster_words, embeddings_dict):
    cluster_words_matrix = np.array([embeddings_dict[w] for w in cluster_words])
    dot_products = np.dot(cluster_words_matrix, past_guesses_matrix.T)
    norms = np.linalg.norm(cluster_words_matrix, axis=1)[:, np.newaxis] * np.linalg.norm(past_guesses_matrix, axis=1)
    similarities = dot_products / norms
    return similarities
# def choose_word_from_cluster_modified(guessed_words, past_guesses_matrix, cluster_words, unused_words, embeddings_dict):
#     if not guessed_words or not unused_words:
#         chosen_word = random.choice(list(unused_words))
#         unused_words.remove(chosen_word)
#         return chosen_word

#     similarities = similarity_matrix(past_guesses_matrix, unused_words, embeddings_dict)
#     best_similarity = np.max(similarities, axis=1)

#     # Adjust the sigmoid function's parameters to emphasize similarity scores
#     sigmoid_weights = 1 / (1 + np.exp(-0.25 * (best_similarity - 40)))

#     weighted_similarities = similarities * sigmoid_weights[:, np.newaxis]
#     total_weights = np.sum(weighted_similarities, axis=1)

#     chosen_word_index = np.argmax(total_weights)
#     chosen_word = list(unused_words)[chosen_word_index]
#     unused_words.remove(chosen_word)
#     return chosen_word
def choose_word_from_cluster_modified(guessed_words, past_guesses_matrix, cluster_words, unused_words, embeddings_dict):
    if not guessed_words or not unused_words:
        chosen_word = random.choice(list(unused_words))
        unused_words.remove(chosen_word)
        return chosen_word

    similarities = similarity_matrix(past_guesses_matrix, unused_words, embeddings_dict)
    best_similarity = np.max(similarities, axis=1)

    # Apply a power function to the similarity scores
    power_weights = best_similarity ** 3

    weighted_similarities = similarities * power_weights[:, np.newaxis]
    total_weights = np.sum(weighted_similarities, axis=1)

    chosen_word_index = np.argmax(total_weights)
    chosen_word = list(unused_words)[chosen_word_index]
    unused_words.remove(chosen_word)
    return chosen_word


