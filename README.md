<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/marc/master/marc.png" width="500px" alt="marc">
</h3>
<p align="center">
  <a href="https://travis-ci.org/maxhumber/marc"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="PyPI" src="https://img.shields.io/pypi/v/marc.svg"></a>
</p>



### About

marc is a **mar**kov **c**hain library for Python and Swift



### Python

Install:

```sh
pip install -U marc
```



Copy and paste this to get started:

```python
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
```



### Swift

SPM:

```swift
dependencies: [
    .package(url: "https://github.com/maxhumber/marc.git", .upToNextMajor(from: "2.0"))
]
```



Quickstart:

```swift
import Marc

let playerThrows = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
let sequence = playerThrows.map { String($0) }

let chain = MarkovChain(sequence)
chain.update("R", "S")

print(chain["R"])
// [("P", 0.5), ("R", 0.25), ("S", 0.25)]

let playerLastThrow = "R"
let playerPredictedNextThrow = chain.next(playerLastThrow)! // << returns optional
print(playerPredictedNextThrow)
// "P"

let counters = ["R": "P", "P": "S", "S": "R"]
let counterThrow = counters[playerPredictedNextThrow]! // << returns optional
print(counterThrow)
// "S"
```



### API/Comparison

|                                         | Python                                 | Swift                                      |
| --------------------------------------- | -------------------------------------- | ------------------------------------------ |
| **Initialize**                          | `chain = MarkovChain()`                | `chain = MarkovChain<String>()`            |
| **Initialize** (with starting sequence) | `chain = MarkovChain(["R", "P", "S"])` | `let chain = MarkovChain(["R", "P", "S"])` |
| **Update** chain                        | `chain.update("R", "P")`               | `chain.update("R", "P")`                   |
| **Lookup** state                        | `chain["R"]`                           | `chain["R"]`                               |
| Generate **next**                       | `chain.next("R")`                      | `chain.next("R")!`                         |



### Shakespeare

Python:

```python
import random
import re
from marc import MarkovChain

text = ""
with open("python/demo/shakespeare.txt", "r") as f:
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
```

