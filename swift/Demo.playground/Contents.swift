// MARK: - Example 1

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


// MARK: - Example 2

import Foundation
import Marc

func loadShakespeare() throws -> String {
    guard let fileUrl = Bundle.main.url(forResource: "shakespeare", withExtension: "txt") else { fatalError() }
    return try String(contentsOf: fileUrl, encoding: String.Encoding.utf8)
}

let text = try! loadShakespeare()
let tokens = text.split(separator: " ")

let chain2 = MarkovChain(tokens)
chain2["Hamlet"]
chain2.next("Hamlet")
