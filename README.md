<h3 align="center">
  <img alt="marc" src="images/logo.png" height="125px">
</h3>
<div align="center">
</div>






### About

marc is a **mar**kov **c**hain generator for python and/or swift



### Python

Install<sup>‡</sup>

```sh
pip install marc
```



Quickstart:

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

For more inspiration see the [python/examples/](python/examples/) directory



### Swift

SPM:

```swift
dependencies: [
    .package(url: "https://github.com/maxhumber/marc.git", .upToNextMajor(from: "3.0"))
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
let playerPredictedNextThrow = chain.next(playerLastThrow)!

let counters = ["R": "P", "P": "S", "S": "R"]
let counterThrow = counters[playerPredictedNextThrow]!
print(counterThrow)
// "S"
```

For more inspiration see the [swift/examples/](swift/examples/) directory



### API/Comparison

|                                  | Python                                 | Swift                                      |
| -------------------------------- | -------------------------------------- | ------------------------------------------ |
| Import                           | `from marc import MarkovChain`         | `import Marc`                              |
| Initialize chain                 | `chain = MarkovChain()`                | `chain = MarkovChain<String>()`            |
| Initialize chain (with sequence) | `chain = MarkovChain(["R", "P", "S"])` | `let chain = MarkovChain(["R", "P", "S"])` |
| Update chain                     | `chain.update("R", "P")`               | `chain.update("R", "P")`                   |
| Lookup transitions               | `chain["R"]`                           | `chain["R"]`                               |
| Generate next                    | `chain.next("R")`                      | `chain.next("R")!`                         |



### Fineprint

<sup>‡</sup> marc 3.0+ is incompatible with marc 2.x
