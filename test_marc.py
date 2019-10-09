import pytest

from marc import ListEncoder, MarkovChain

"""
throws = [
    'scissors', 'paper', 'paper', 'paper', 'paper', 'scissors', 'scissors',
    'paper', 'rock', 'scissors', 'rock', 'rock', 'scissors', 'paper', 'rock',
    'rock', 'paper', 'rock', 'scissors', 'scissors', 'paper', 'paper'
]
"""


@pytest.fixture
def throws():
    return [
        "scissors",
        "paper",
        "paper",
        "paper",
        "paper",
        "scissors",
        "scissors",
        "paper",
        "rock",
        "scissors",
        "rock",
        "rock",
        "scissors",
        "paper",
        "rock",
        "rock",
        "paper",
        "rock",
        "scissors",
        "scissors",
        "paper",
        "paper",
    ]


def test_list_encoder(throws):
    le = ListEncoder()
    encoded = le.fit_transform(throws)
    decoded = le.inverse_transform(encoded)
    assert throws == decoded


def test_markov_chain_state_doesnt_exist(throws):
    m = MarkovChain(throws)
    with pytest.raises(TypeError):
        m.next("✂️")


def test_markov_chain_no_current_state(throws):
    m = MarkovChain(throws)
    next_state = m.next()
    assert isinstance(next_state, str)


def test_markov_chain(throws):
    m = MarkovChain(throws)
    next_state = m.next("scissors")
    assert next_state in ["rock", "paper", "scissors"]


def test_markov_chain_with_size(throws):
    m = MarkovChain(throws)
    next_states = m.next("paper", n=2)
    assert len(next_states) == 2
