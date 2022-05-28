import Foundation

public class MarkovChain<Element: Hashable> {
    private typealias Store = [Element: [Element: UInt]]
    
    private var store = Store()
    
    public init() {}

    /// Initialize chain with sequence of elements
    ///
    /// Example:
    /// ```
    /// let chain = MarkovChain(["R", "P", "S"])
    /// ```
    public init<S: Sequence>(_ sequence: S) where S.Element == Element {
        // reducing per: https://developer.apple.com/documentation/swift/dictionary/3127177-reduce
        store = zip(sequence, sequence.dropFirst(1)).reduce(into: Store()) { result, pair in
            result[pair.0, default: [:]][pair.1, default: 0] += 1
        }
    }

    /// Lookup transition probabilities for state
    ///
    /// Example:
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
    /// - Parameters:
    ///   - a: Transition from state
    ///   - b: Transition to state
    ///
    /// Example:
    /// ```
    /// chain.update("R", "B")
    /// ```
    public func update(_ a: Element, _ b: Element) {
        store[a, default: [:]][b, default: 0] += 1
    }

    /// Generate next state from chain
    ///
    /// - Parameters:
    ///   - after: Generate following state
    ///
    /// Example:
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
