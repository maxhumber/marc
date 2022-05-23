from marc import MarkovChain
import pytest

print("WTF pytest")

@pytest.fixture
def sequence():
    player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
    sequence = [throw for throw in player_throws]
    return sequence


def test_lookup(sequence):
    chain = MarkovChain(sequence)
    result = chain["R"]
    print(result)



def test_chain_next_method_seeded(sequence):
    chain = MarkovChain(sequence)
    state = chain.next("x")
    assert state in ["x", "o"]


def test_chain_next_multiple_unseeded(sequence):
    chain = MarkovChain(sequence)
    N = 10000
    results = chain.next(n=N)
    results = [0 if r == "x" else 1 for r in results]
    result = sum(results) / N
    print(result)
    assert 0 < result < 0.35
