import random
from collections import Counter

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

def chain_to_matrix(chain):
    counts = Counter(zip(chain, chain[1:]))
    unique = len(set(chain))
    matrix = [[0 for _ in range(unique)] for _ in range(unique)]
    for (x, y), count in counts.items():
        matrix[x][y] = count
    return matrix

def normalize(x):
    x_sum = sum(x)
    return [i / x_sum for i in x]

def normalize_matrix(matrix):
    normalized_matrix = []
    for row in matrix:
        normalized_row = normalize(row)
        normalized_matrix.append(normalized_row)
    return normalized_matrix

def chain_to_transition_matrix(chain):
    matrix = chain_to_matrix(chain)
    transition_matrix = normalize_matrix(matrix)
    return transition_matrix

class MarkovChain:
    def __init__(self, chain):
        self.encoder = ListEncoder()
        encoded_chain = self.encoder.fit_transform(chain)
        self.transition_matrix = chain_to_transition_matrix(encoded_chain)

    def next_state(self, current_state):
        encoded_state = self.encoder.transform(current_state)
        probs = self.transition_matrix[encoded_state]
        random_next = random.choices(range(len(probs)), weights=probs)[0]
        return self.encoder.inverse_transform(random_next)

    def generate_states(self, current_state=None, n=10):
        if not current_state:
            possible = list(self.encoder.encoder.keys())
            current_state = random.choice(possible)
        future_states = []
        for _ in range(n):
            random_next = self.next_state(current_state)
            future_states.append(random_next)
            current_state = random_next
        return future_states
