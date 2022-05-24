from unittest import TestCase
from marc import MarkovChain


class TestMarc(TestCase):
    def setUp(self):
        player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
        sequence = [throw for throw in player_throws]
        self.chain = MarkovChain(sequence)

    def test_lookup(self):
        result = self.chain["R"]["P"]
        self.assertAlmostEqual(result, 0.5217391304347826)

    def test_update(self):
        self.chain.update("R", "S")
        probs = self.chain["R"]
        rock = probs["R"]
        self.assertEqual(rock, 0.25)

    def test_next(self):
        next_state = self.chain.next("R")
        self.assertTrue(next_state in ["R", "P", "S"])


if __name__ == "__main__":
    unittest.main()
