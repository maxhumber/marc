from collections import defaultdict
import random


class MarkovChain:
    def __init__(self, sequence=None):
        self._store = defaultdict(lambda: defaultdict(lambda: 0))
        if not sequence:
            return
        for a, b in zip(sequence, sequence[1:]):
            self.update(a, b)

    def __getitem__(self, element):
        options = sorted(self._store[element].items(), key=lambda i: -i[1])
        total = sum(self._store[element].values())
        return {option: weight/total for (option, weight) in options}

    def update(self, a, b):
        self._store[a][b] += 1

    def next(self, after):
        options = list(self._store[after].keys())
        weights = self._store[after].values()
        return random.choices(options, weights, k=1)[0]
