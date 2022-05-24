from collections import defaultdict
import random


class MarkovChain:
    def __init__(self, sequence=None):
        """Initialize chain with/without starting sequence

        Examples:
        ```
        chain = MarkovChain(["R", "P", "S"])
        chain2 = MarkovChain()
        ```
        """
        self._store = defaultdict(lambda: defaultdict(lambda: 0))
        if not sequence:
            return
        for a, b in zip(sequence, sequence[1:]):
            self.update(a, b)

    def __getitem__(self, state):
        """Fetch transition probabilities for state

        Example:
        ```
        probs = chain["R"]
        ```
        """
        options = sorted(self._store[state].items(), key=lambda i: -i[1])
        total = sum(self._store[state].values())
        return {option: weight / total for (option, weight) in options}

    def update(self, a, b):
        """Update chain with transition a -> b

        Example:
        ```
        chain.update("R", "P")
        ```
        """
        self._store[a][b] += 1

    def next(self, after):
        """Generate next state from chain

        Example:
        ```
        chain.next("R")
        ```
        """
        options = list(self._store[after].keys())
        weights = self._store[after].values()
        return random.choices(options, weights, k=1)[0]
