import Foundation

public class MarkovChain<Element: Hashable> {
    private var store: [Element: [Element: UInt]] = [:]
    
    public init() {}

    /// Initialize chain with starting sequence of generic elements
    ///
    /// - Example:
    /// ```
    /// let chain = MarkovChain(["R", "P", "S"])
    /// ```
    public init(_ sequence: [Element]) {
        zip(sequence, sequence[1...]).forEach { update($0.0, $0.1) }
    }

    /// Fetch transition probabilities for state
    ///
    /// - Example:
    /// ```
    /// let transitionProbabilities = chain["R"]
    /// ```
    public subscript(state: Element) -> [(Element, Double)] {
        let options = store[state, default: [:]]
        let total = options.values.reduce(0, +)
        return options
            .sorted { $0.value > $1.value }
            .map { ($0.key, Double($0.value) / Double(total)) }
    }

    /// Update chain with transition a -> b
    ///
    /// - Example:
    /// ```
    /// chain.update("R", "B")
    /// ```
    public func update(_ a: Element, _ b: Element) {
        // TODO: speed this up cause it slow AF
        store[a, default: [:]][b, default: 0] += 1
    }

    /// Generate next state from chain
    ///
    /// - Example:
    /// ```
    /// let nextState = chain.next("R")
    /// ```
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
