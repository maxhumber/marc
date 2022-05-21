import XCTest
@testable import Marc

final class MarcTests: XCTestCase {
    func testExample() throws {
        let chain = MarkovChain<String>()
        chain.update("R", "P")
        chain.update("R", "P")
        chain.update("R", "P")
        chain.update("R", "R")
        chain.update("R", "S")
        chain.update("R", "S")
        chain.update("R", "S")
        chain.update("S", "S")
        chain.next("R")
        chain["R"]
    }
    
    func testExample2() throws {
        let sequence = [
            "Rock", "Rock", "Rock", "Paper", "Rock", "Scissors",
            "Paper", "Paper", "Scissors", "Rock", "Scissors",
            "Scissors", "Paper", "Scissors", "Rock", "Rock", "Rock",
            "Paper", "Scissors", "Scissors", "Scissors", "Rock"
        ]
        
        let chain2 = MarkovChain(sequence)

        var outputs = [String]()
        var input = "Rock"
        for _ in 0..<10 {
            if let output = chain2.next(input) {
                outputs.append(output)
                input = output
            }
        }
        
        print(outputs)
    }
}
