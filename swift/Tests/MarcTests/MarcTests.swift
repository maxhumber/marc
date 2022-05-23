import XCTest
@testable import Marc

final class MarcTests: XCTestCase {
    var chain: MarkovChain<String>!
    
    override func setUp() {
        let playerThrows = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
        let sequence = playerThrows.map { String($0) }
        chain = MarkovChain(sequence)
    }

    func testSubscript() {
        let probs = chain["R"]
        let paperProb = probs[0].1
        XCTAssertEqual(paperProb, 0.5217391304347826)
    }
    
    func testUpdate() {
        chain.update("R", "S")
        let probs = chain["R"]
        let rockProb = probs[2].1
        XCTAssertEqual(rockProb, 0.25)
    }
    
    func testNext() {
        let next = chain.next("R")!
        let contains = ["R", "P", "S"].contains(next)
        XCTAssertTrue(contains)
    }
    
    func testPerformanceExample() throws {
        var sequence = [Int]()
        for _ in 0...1_000_000 {
            let random = Int.random(in: 1...3)
            sequence.append(random)
        }
        self.measure {
            let chain = MarkovChain(sequence)
        }
    }
}
