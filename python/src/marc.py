from collections import defaultdict
import random


class MarkovChain:
    def __init__(self, sequence=None):
        self.store = defaultdict(lambda: defaultdict(lambda: 0))
        if not sequence:
            return
        for a, b in zip(sequence, sequence[1:]):
            self.update(a, b)

    def update(self, a, b):
        self.store[a][b] += 1

    def next(self, after):
        options = list(self.store[after].keys())
        weights = self.store[after].values()
        return random.choices(options, weights, k=1)[0]
