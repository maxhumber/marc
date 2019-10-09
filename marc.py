import random

class MarkovChain:
    '''A simple Markov chain generator

    Attributes:

    - current_state (str): The current state in the chain
    - encoder (ListEncoder): The object that transforms the chain
    - transition_matrix (list): The matrix that drives the chain

    Methods:

    - next: Generate the next state from the chain

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

        - chain (list): Collection to convert to a Markov chain
        '''
        self.encoder = ListEncoder()
        encoded_chain = self.encoder.fit_transform(chain)
        self.transition_matrix = self._chain_to_matrix(encoded_chain)
        self.current_state = None

    def __repr__(self):
        return 'MarkovChain()'

    def __iter__(self):
        return self

    def __next__(self):
        self.current_state = self.next(self.current_state)
        return self.current_state

    def next(self, current_state=None, n=1):
        '''Generate the next state from the chain

        Params:

        - current_state (str, optional): Seed state
        - n (int): Number of states to generate

        Examples:

        ```
        sequence = [1, 1, 2, 3, 2, 1, 2, 1, 3, 1]
        chain = MarkovChain(sequence)

        chain.next(1)
        # 2

        chain.next(3, n=5)
        # [2, 1, 3, 2, 1]
        ```
        '''
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

    @staticmethod
    def _chain_to_matrix(chain):
        unique = len(set(chain))
        matrix = [[0] * unique for _ in range(unique)]
        for (x, y) in zip(chain, chain[1:]):
            matrix[x][y] += 1
        for row in matrix:
            rsum = sum(row)
            if rsum > 0:
                row[:] = [i / rsum for i in row]
        return matrix

class ListEncoder:
    '''List to Integer Transformer

    Methods:

    - fit: Create/learn the integer index lookup
    - transform: Transform the list according to the index
    - fit_transform: fit and transform
    - inverse_transform: Reverse the index lookup

    Attributes:

    - index_: Integer lookup learned by fit

    Example:

    ```
    encoder = ListEncoder()
    sequence = ['rock', 'paper', 'scissors', 'scissors', 'paper']
    encoder.fit_transform(sequence)
    # [1, 2, 0, 0, 2]
    encoder.inverse_transform(1)
    # 'rock'
    ```
    '''

    def __repr__(self):
        return 'ListEncoder()'

    def __dir__(self):
        return ['fit', 'transform', 'fit_transform', 'index_']

    def fit(self, y):
        '''Fit the Transformer

        Params:

        - y (list): Collection to index
        '''
        self.index_ = {v:k for k, v in enumerate(set(y))}
        self.decoder = {v:k for k, v in self.index_.items()}
        return self

    def transform(self, y):
        '''Transform according to the learned index

        Params:

        - y (str|list): Item or collection to transform
        '''
        if not isinstance(y, list):
            return self.index_.get(y)
        return [self.index_.get(yi) for yi in y]

    def fit_transform(self, y):
        '''Fit and transform

        Params:

        - y (list): Collection to fit and transform
        '''
        self.fit(y)
        return self.transform(y)

    def inverse_transform(self, y):
        '''Reverse the transform

        Params:

        - y (str|list): Item or collection to reverse lookup
        '''
        if not isinstance(y, list):
            return self.decoder.get(y)
        return [self.decoder.get(yi) for yi in y]
