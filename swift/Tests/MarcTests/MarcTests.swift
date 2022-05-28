import XCTest
@testable import Marc

final class MarcTests: XCTestCase {
    var chain: MarkovChain<String>!
    
    typealias PerfStore = [Int: [Int: Int]]
    let perfSeq = (0..<10_000).map { _ in Int.random(in: 1...5) }
    var perfStore: PerfStore!
    
    override func setUp() {
        let playerThrows = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
        let sequence = playerThrows.map { String($0) }
        chain = MarkovChain(sequence)
        perfStore = PerfStore()
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
    
    func testStorePerformance() {
       measure {
           perfStore = zip(perfSeq, perfSeq.dropFirst(1)).reduce(into: PerfStore()) { result, pair in
               result[pair.0, default: [:]][pair.1, default: 0] += 1
           }
        }
    }
}
