from marc import MarkovChain
import pytest


@pytest.fixture
def chain():
    player_throws = "RRRSRSRRPRPSPPRPSSSPRSPSPRRRPSSPRRPRSRPRPSSSPRPRPSSRPSRPRSSPRP"
    sequence = [throw for throw in player_throws]
    return MarkovChain(sequence)


def test_lookup(chain):
    result = chain["R"]["P"]
    assert result == 0.5217391304347826


def test_update(chain):
    chain.update("R", "S")
    probs = chain["R"]
    rock = probs["R"]
    assert rock == 0.25


def test_next(chain):
    next = chain.next("R")
    assert next in ["R", "P", "S"]
