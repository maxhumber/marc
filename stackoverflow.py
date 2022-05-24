from collections import defaultdict
import random

sequence = []
for _ in range(10_000):
    rand = random.choice([1, 2, 3])
    sequence.append(rand)

my_dict = defaultdict(lambda: defaultdict(lambda: 0))
for a, b in zip(sequence, sequence[1:]):
    my_dict[a][b] += 1

my_dict
