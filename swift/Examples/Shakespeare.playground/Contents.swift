import Foundation
import NaturalLanguage
import Marc

let fileUrl = Bundle.main.url(forResource: "shakespeare", withExtension: "txt")!
let text = try! String(contentsOf: fileUrl, encoding: .utf8)

let tokenizer = NLTokenizer(unit: .word)
tokenizer.string = text
let tokens = tokenizer.tokens(for: text.startIndex..<text.endIndex).map { String(text[$0]) }

let chain = MarkovChain(tokens)

var word = tokens.randomElement()!
// "Who"

print(chain[word])
//[("is", 0.07806191117092867), ("hath", 0.026917900403768506), ...]

var words = [String]()
for _ in 0..<25 {
    words.append(word)
    word = chain.next(word)!
}

let sentence = words.joined(separator: " ")
print(sentence)
// "Who in desolation Touching the old I am sunburnt and but some hedge corner of that I cry Amen Amen I am a man like"
