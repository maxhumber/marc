import Foundation

class MarkovChain<Element: Hashable> {
    private var store: [Element: [Element: UInt]] = [:]
    
    init() {}
    
    init(_ sequence: [Element]) {
        zip(sequence, sequence[1...]).forEach { update($0.0, $0.1) }
    }
    
    subscript(element: Element, normalized: Bool = true) -> [(Element, Double)] {
        let options = store[element, default: [:]]
        if normalized {
            let total = options.values.reduce(0, +)
            return options
                .sorted { $0.value > $1.value }
                .map { ($0.key, Double($0.value) / Double(total)) }
        }
        return options.map { ($0.key, Double($0.value)) }
    }
    
    func update(_ a: Element, _ b: Element) {
        store[a, default: [:]][b, default: 0] += 1
    }
    
    func next(_ after: Element) -> Element? {
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
