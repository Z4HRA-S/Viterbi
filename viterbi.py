def decode(obs_seq, transition_matrix, emission_matrix, states, initial_probs):
    st_l=len(states)
    obs_l=len(obs_seq)
    max_prob = [[0] * obs_l for _ in range(st_l)]
    arg_max_prob = [[0] * obs_l for _ in range(st_l)]

    for i in range(st_l):
        max_prob[i][0] = initial_probs[states[i]]

    for j in range(1, obs_l):
        for i in range(st_l):
            max_prob_p = 0
            arg_max = 0
            for k in range(st_l):
                new_prob = (max_prob[k][j - 1]
                            * transition_matrix[states[k]][states[i]]
                            * emission_matrix[states[i]][obs_seq[j]])
                if new_prob >= max_prob_p:
                    max_prob_p = new_prob
                    arg_max = k

            max_prob[i][j] = max_prob_p
            arg_max_prob[i][j] = arg_max

    last_obs = [x[obs_l - 1] for x in max_prob]
    state_index = last_obs.index(max(last_obs))
    last_state = states[state_index]
    hidden_states = []

    for i in range(obs_l - 1, 0, -1):
        state_index = arg_max_prob[state_index][i]
        hidden_states.append(states[state_index])

    hidden_states.append(last_state)
    print(max_prob)

    return hidden_states


if __name__ == "__main__":
    obs = ('normal', 'cold', 'dizzy')
    state = ('Healthy', 'Fever')
    start_p = {'Healthy': 0.6, 'Fever': 0.4}
    trans_p = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6}
    }
    emit_p = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
    }

    path_matrix = decode(obs, trans_p, emit_p, state, start_p)
    print(path_matrix)