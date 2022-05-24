from marc import MarkovChain
from unittest import TestCase

class TestMarc(TestCase):
    def chain(self):
        player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
        sequence = [throw for throw in player_throws]
        chain = MarkovChain(sequence)
        print(test)
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()

#
# def test_lookup(chain):
#     result = chain["R"]["P"]
#     assert result == 0.5217391304347826
#
#
# def test_update(chain):
#     chain.update("R", "S")
#     probs = chain["R"]
#     rock = probs["R"]
#     assert rock == 0.25
#
#
# def test_next(chain):
#     next = chain.next("R")
#     assert next in ["R", "P", "S"]
