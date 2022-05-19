import Foundation

class MarkovChain<Element: Hashable> {
    private var store: [Element: [Element: UInt]] = [:]
    
    init() {}
    
    init(_ sequence: [Element]) {
        zip(sequence, sequence[1...]).forEach { update($0.0, $0.1) }
    }
    
    subscript(a: Element) -> [Element: UInt] {
        store[a, default: [:]]
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
