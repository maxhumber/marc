import Foundation
import Marc

func loadShakespeare() throws -> String {
    guard let fileUrl = Bundle.main.url(forResource: "shakespeare", withExtension: "txt") else { fatalError() }
    return try String(contentsOf: fileUrl, encoding: String.Encoding.utf8)
}

let text = try! loadShakespeare()

extension String {
    func words() -> [String] {
        
        let range = Range<String.Index>(start: self.startIndex, end: self.endIndex)
        var words = [String]()
        
        self.enumerateSubstringsInRange(range, options: NSStringEnumerationOptions.ByWords) { (substring, _, _, _) -> () in
            words.append(substring)
        }
        
        return words
    }
}

////


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
