import Foundation

var sequence = (0..<10_000).map { _ in Int.random(in: 1...5) }

var dict: [Int: [Int: Int]] = [:]
zip(sequence, sequence[1...]).reduce(into: Dictionary<Int, Dictionary<Int, Int>>()) { partialResult, pair in
    partialResult[pair.0, default: [:]][pair.1, default: 0] += 1
}

for (a, b) in zip(sequence, sequence[1...]) {
    dict[a, default: [:]][b, default: 0] += 1
}

//







//
///// other options
//
//var options = store[a] ?? [:]
//let value = options[b] ?? 0
//options[b] = value + 1
//store[a] = options
//store
//
//
//let value2 = store[a]?[b] ?? 0
//store[a]![b] = value2 + 1
//store

