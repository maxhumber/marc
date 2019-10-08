import random

class MarkovChain:
    def __init__(self, chain):
        self.encoder = ListEncoder()
        encoded_chain = self.encoder.fit_transform(chain)
        self.transition_matrix = chain_to_transition_matrix(encoded_chain)

    def next(self, current_state=None, n=1):
        if not current_state:
            possible = list(self.encoder.encoder.keys())
            current_state = random.choice(possible)
        future_states = []
        for _ in range(n):
            encoded_state = self.encoder.transform(current_state)
            probs = self.transition_matrix[encoded_state]
            random_next = random.choices(range(len(probs)), weights=probs)[0]
            random_next = self.encoder.inverse_transform(random_next)
            future_states.append(random_next)
            current_state = random_next
        if n == 1:
            return future_states[0]
        return future_states

def chain_to_matrix(chain):
    unique = len(set(chain))
    matrix = [[0] * unique for _ in range(unique)]
    for (x, y) in zip(chain, chain[1:]):
        matrix[x][y] += 1
    return matrix

def normalize_matrix(matrix):
    for row in matrix:
        rsum = sum(row)
        if rsum > 0:
            row[:] = [i / rsum for i in row]
    return matrix

def chain_to_transition_matrix(chain):
    matrix = chain_to_matrix(chain)
    transition_matrix = normalize_matrix(matrix)
    return transition_matrix

class ListEncoder:
    def fit(self, y):
        self.encoder = {v:k for k, v in enumerate(set(y))}
        return self

    def transform(self, y):
        if not isinstance(y, list):
            return self.encoder.get(y)
        return [self.encoder.get(yi) for yi in y]

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

    def inverse_transform(self, y):
        decoder = {v:k for k, v in self.encoder.items()}
        if not isinstance(y, list):
            return decoder.get(y)
        return [decoder.get(yi) for yi in y]
