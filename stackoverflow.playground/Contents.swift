import Foundation

typealias Element = String

var store: [Element: [Element: UInt]] = [:]

let a = "R"
let b = "P"
store[a, default: [:]][b, default: 0] += 1
store

var options = store[a] ?? [:]
let value = options[b] ?? 0
options[b] = value + 1
store[a] = options
store


let value2 = store[a]?[b] ?? 0
store[a]![b] = value2 + 1
store
