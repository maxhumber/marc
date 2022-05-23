import random
import re
from marc import MarkovChain

text = ""
with open("python/examples/shakespeare.txt", "r") as f:
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

sentence = re.sub(r'\s([?.!,;_"](?:\s|$))', r"\1", " ".join(words))
# 'Who is not being sensible in men what shall I shall attend him; then. Fear you love our brother, or both friend'
