import viterbi


def test1():
    states = ('Rainy', 'Sunny')

    observations = ('walk', 'shop', 'clean')

    start_probability = {'Rainy': 0.6, 'Sunny': 0.4}

    transition_probability = {
        'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
        'Sunny': {'Rainy': 0.4, 'Sunny': 0.6},
    }

    emission_probability = {
        'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
        'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1},
    }

    path_matrix = viterbi.decode(observations, transition_probability, emission_probability, states,
                                    start_probability)

    print(path_matrix)


def test2():
    obs = ('normal', 'cold', 'dizzy')
    states = ('Healthy', 'Fever')
    start_p = {'Healthy': 0.6, 'Fever': 0.4}
    trans_p = {
        'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
        'Fever': {'Healthy': 0.4, 'Fever': 0.6}
    }
    emit_p = {
        'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
        'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6}
    }

    path_matrix = viterbi.decode(obs, trans_p, emit_p, states, start_p)
    print(path_matrix)
