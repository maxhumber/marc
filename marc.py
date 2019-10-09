import random

class MarkovChain:
    '''A simple Markov chain generator

    Attributes:

    - current_state (str): The current state in the chain
    - encoder (ListEncoder):
    - transition_matrix (list(list)): The matrix that drives the chain

    Methods:

    chain.encoder.encoder

    - next:

    Examples:

    ```
    sequence = [1, 1, 2, 3, 2, 1, 2, 1, 3, 1]
    chain = MarkovChain(sequence)

    chain.next(1)
    # 2

    next(chain)
    # 1

    chain.next(3, n=5)
    # [2, 1, 3, 2, 1]
    ```
    '''
    def __init__(self, chain):
        '''Params:

        - chain (list):
        '''
        self.encoder = ListEncoder()
        encoded_chain = self.encoder.fit_transform(chain)
        self.transition_matrix = chain_to_transition_matrix(encoded_chain)
        self.current_state = None

    def __repr__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        self.current_state = self.next(self.current_state)
        return self.current_state

    def next(self, current_state=None, n=1):
        if not current_state:
            possible = list(self.encoder.index_.keys())
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
    def __repr__(self):
        return 'ListEncoder()'

    def __dir__(self):
        return ['fit', 'transform', 'fit_transform', 'index_']

    def fit(self, y):
        self.index_ = {v:k for k, v in enumerate(set(y))}
        self.decoder = {v:k for k, v in self.index_.items()}
        return self

    def transform(self, y):
        if not isinstance(y, list):
            return self.index_.get(y)
        return [self.index_.get(yi) for yi in y]

    def fit_transform(self, y):
        self.fit(y)
        return self.transform(y)

    def inverse_transform(self, y):
        if not isinstance(y, list):
            return self.decoder.get(y)
        return [self.decoder.get(yi) for yi in y]
