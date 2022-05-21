from marc import MarkovChain
import pytest


@pytest.fixture
def sequence():
    sequence = [i for i in "xxxxxoxxxxxxoooxxxxo"]
    return sequence


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
