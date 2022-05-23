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
