import Foundation

public class MarkovChain<Element: Hashable> {
    private var store: [Element: [Element: UInt]] = [:]
    
    /// Bare initializer (use .update to seed chain)
    public init() {}

    /// Initialize chain with a sequence of generic elements
    public init(_ sequence: [Element]) {
        zip(sequence, sequence[1...]).forEach { update($0.0, $0.1) }
    }

    /// Fetch transition probabilities for a specific element/state
    public subscript(element: Element) -> [(Element, Double)] {
        let options = store[element, default: [:]]
        let total = options.values.reduce(0, +)
        return options
            .sorted { $0.value > $1.value }
            .map { ($0.key, Double($0.value) / Double(total)) }
    }

    /// Update chain with a new transition from a -> b
    public func update(_ a: Element, _ b: Element) {
        store[a, default: [:]][b, default: 0] += 1
    }

    /// Fetch a generated next state from the chain
    public func next(_ after: Element) -> Element? {
        let options = store[after, default: [:]]
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
