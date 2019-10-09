import random


class MarkovChain:
    """Markov chain generator

    Attributes:

    - state (str): The current state in the chain
    - encoder (ListEncoder): The object that manages and transforms the sequence
    - matrix (list): The transition matrix that drives the chain

    Methods:

    - next: Generate the next state

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
    """

    def __init__(self, sequence):
        """Params:

        - sequence (list): Sequence to convert into a Markov chain
        """
        self.encoder = ListEncoder()
        encoded_sequence = self.encoder.fit_transform(sequence)
        self.matrix = self._sequence_to_matrix(encoded_sequence)
        self.state = None

    def __repr__(self):
        return "MarkovChain()"

    def __iter__(self):
        return self

    def __next__(self):
        self.state = self.next(self.state)
        return self.state

    def next(self, state=None, n=1):
        """Generate the next state

        Params:

        - state (str, optional): The starting/seed state
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
        """
        if not state:
            possible = list(self.encoder.index_.keys())
            state = random.choice(possible)
        self.state = state
        states = []
        for _ in range(n):
            encoded_state = self.encoder.transform(self.state)
            probs = self.matrix[encoded_state]
            next_state = random.choices(range(len(probs)), weights=probs)[0]
            next_state = self.encoder.inverse_transform(next_state)
            states.append(next_state)
            self.state = next_state
        if n == 1:
            return states[0]
        return states

    @staticmethod
    def _sequence_to_matrix(sequence):
        unique = len(set(sequence))
        matrix = [[0] * unique for _ in range(unique)]
        for (x, y) in zip(sequence, sequence[1:]):
            matrix[x][y] += 1
        for row in matrix:
            rsum = sum(row)
            if rsum > 0:
                row[:] = [i / rsum for i in row]
        return matrix


class ListEncoder:
    """List to Integer Transformer

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
    """

    def __repr__(self):
        return "ListEncoder()"

    def __dir__(self):
        return ["fit", "transform", "fit_transform", "index_"]

    def fit(self, y):
        """Fit the Transformer

        Params:

        - y (list): Collection to index
        """
        self.index_ = {v: k for k, v in enumerate(set(y))}
        self.decoder = {v: k for k, v in self.index_.items()}
        return self

    def transform(self, y):
        """Transform according to the learned index

        Params:

        - y (str|list): Item or collection to transform
        """
        if not isinstance(y, list):
            return self.index_.get(y)
        return [self.index_.get(yi) for yi in y]

    def fit_transform(self, y):
        """Fit and transform

        Params:

        - y (list): Collection to fit and transform
        """
        self.fit(y)
        return self.transform(y)

    def inverse_transform(self, y):
        """Reverse the transform

        Params:

        - y (str|list): Item or collection to reverse lookup
        """
        if not isinstance(y, list):
            return self.decoder.get(y)
        return [self.decoder.get(yi) for yi in y]
