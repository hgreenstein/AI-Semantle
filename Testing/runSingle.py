def run_single_game(mystery_word, q_agent, max_guesses, shared_q_table):
    q_agent.q_table = shared_q_table
    env = environment(mystery_word, clusters)
    state = tuple(env.get_state())
    similarity_score = 0
    game_wins_local = 0
    total_moves_local = 0

    for i in range(max_guesses):
        if similarity_score != 100:
            action = q_agent.choose_action(state)
            word = choose_word_from_cluster(env.clusters[action], env.guessed_words)
            similarity_score = env.guess_word(word, action)
            next_state = tuple(env.get_state())
            reward = env.get_reward(similarity_score, i, max_guesses, word)
            q_agent.update(state, action, reward, next_state)
            state = next_state
        else:
            reward = env.get_reward(similarity_score, i, max_guesses, word)
            q_agent.update(state, action, reward, next_state)
            game_wins_local = 1
            total_moves_local = i
            similarity_score = 0
            break
    env.guessed_words = []
    q_agent.decayEpsilon(num_game)
    return game_wins_local, total_moves_local