import Foundation

class MarkovChain<Element: Hashable> {
    var store: [Element: [Element: UInt]] = [:]
    
    init() {}
    
    init(_ sequence: [Element]) {
        for (a, b) in zip(sequence, sequence[1...]) {
            update(a, b)
        }
    }
    
    subscript(a: Element) -> [Element: UInt] {
        store[a, default: [:]]
    }
    
    func update(_ a: Element, _ b: Element) {
        store[a, default: [:]][b, default: 0] += 1
    }
    
    func after(_ a: Element) -> Element? {
        let options = store[a, default: [:]]
        let total = options.values.reduce(0, +)
        let rand = UInt(arc4random_uniform(UInt32(total)))
        var sum = UInt(0)
        for (option, weight) in options {
            sum += weight
            if rand < sum {
                return option
            }
        }
        return nil
    }
}

let chain = MarkovChain<String>()
chain.update("R", "P")
chain.update("R", "P")
chain.update("R", "P")
chain.update("R", "R")
chain.update("R", "S")
chain.update("R", "S")
chain.update("R", "S")
chain.update("S", "S")
chain.after("R")
chain.after("R")
chain.after("R")
chain.after("S")
chain["R"]

let sequence = [
    "Rock", "Rock", "Rock", "Paper", "Rock", "Scissors",
    "Paper", "Paper", "Scissors", "Rock", "Scissors",
    "Scissors", "Paper", "Scissors", "Rock", "Rock", "Rock",
    "Paper", "Scissors", "Scissors", "Scissors", "Rock"
]

let chain2 = MarkovChain(sequence)
chain2.after("Rock")
chain2.after("Rock")
chain2.after("Rock")
chain2.after("Rock")
chain2.after("Rock")
chain2.after("Rock")



print(chain.store)


