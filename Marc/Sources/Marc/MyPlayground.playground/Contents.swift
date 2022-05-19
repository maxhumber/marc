import Foundation

struct MarkovPair {
    var from: String
    var to: String
}

class MarkovChain {
    var store: [String: [String: Int]] = [:]
    
    func add(from: String, to: String) {
        store[from, default: [:]][to, default: 0] += 1
    }
}

let chain = MarkovChain()
chain.add(from: "R", to: "P")
print(chain.store)


var store: [String: [String: Int]] = [:]

let pair = MarkovPair(from: "R", to: "P")

store["R"] = [:]
store["R"]?["P"] = 1
if let value = store["R"]?["P"] {
    store["R"]?["P"] = value + 1
}

store["R", default: [:]]["P", default: 0] += 1
store["R", default: [:]]["R", default: 0] += 1
store


let input = "R"
let output = "S"

store["S", default: [:]]




if let options = store[input] {
    
} else {
    store[input] = [:]
}



print(store)

store["R"]
