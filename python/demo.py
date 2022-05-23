# python -m ipykernel install --user --name="marc.venv"

# Example 1

import random
import re
from marc import MarkovChain

text = ""
with open("data/shakespeare.txt", "r") as f:
    for line in f.readlines():
        text += line

tokens = re.findall(r"[\w']+|[.,!?;]", text)

chain = MarkovChain(tokens)

word = random.choice(tokens)
# 'Who'

chain[word]
# {
#     ',': 0.12915601023017903,
#     'is': 0.08695652173913043,
#     's': 0.05115089514066496,
#     'hath': 0.02557544757033248,
#     'was': 0.021739130434782608,
#     'can': 0.020460358056265986,
#     'shall': 0.01918158567774936,
#     'would': 0.017902813299232736,
#     ...
# }

words = []
for i in range(25):
    words.append(word)
    word = chain.next(word)

sentence = re.sub(r'\s([?.!,;_"](?:\s|$))', r'\1', " ".join(words))
# 'Who is not being sensible in men what shall I shall attend him; then. Fear you love our brother, or both friend'


# Example 2

from marc import MarkovChain

player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
sequence = [throw for throw in player_throws]
# ['R', 'R', 'R', 'S', 'R', 'S', 'R', ...]

chain = MarkovChain(sequence)
chain.update("R", "S")

chain["R"]
# {'P': 0.5, 'R': 0.25, 'S': 0.25}

player_last_throw = "R"
player_predicted_next_throw = chain.next(player_last_throw)
# 'P'

counters = {"R": "P", "P": "S", "S": "R"}
counter_throw = counters[player_predicted_next_throw]
# 'S'
