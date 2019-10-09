import pytest

from marc import ListEncoder, MarkovChain


@pytest.fixture
def sequence():
    sequence = [i for i in "xxxxxoxxxxxxoooxxxxo"]
    return sequence


def test_list_encoder(sequence):
    le = ListEncoder()
    encoded = le.fit_transform(sequence)
    decoded = le.inverse_transform(encoded)
    assert sequence == decoded


def test_list_encoder_transform_one(sequence):
    le = ListEncoder()
    le.fit(sequence)
    t = le.transform("x")
    assert t == 0


def test_list_encoder_transform_multiple(sequence):
    le = ListEncoder()
    le.fit(sequence)
    x = le.transform('x')
    o = le.transform('o')
    l = le.transform(["x", "x", "o"])
    assert l == [x, x, o]


def test_chain_matrix(sequence):
    chain = MarkovChain(sequence)
    x = chain.encoder.index_['x']
    o = chain.encoder.index_['o']
    assert chain.matrix[x][o] == 0.2

# TODO: throw a better error
def test_chain_state_doesnt_exist(sequence):
    chain = MarkovChain(sequence)
    with pytest.raises(TypeError):
        chain.next("y")


def test_chain_state_new(sequence):
    chain = MarkovChain(sequence)
    assert not chain.state


def test_chain_next_iteration(sequence):
    chain = MarkovChain(sequence)
    state = next(chain)
    assert state == chain.state


def test_chain_next_method_seeded(sequence):
    chain = MarkovChain(sequence)
    state = chain.next("x")
    assert state in ["x", "o"]


def test_chain_next_method_unseeded(sequence):
    chain = MarkovChain(sequence)
    state = chain.next()
    assert state in ["x", "o"]


def test_chain_next_multiple_unseeded(sequence):
    chain = MarkovChain(sequence)
    N = 10000
    results = chain.next(n=N)
    results = [0 if r == "x" else 1 for r in results]
    result = sum(results) / N
    print(result)
    assert 0 < result < 0.35


def test_chain_state_after_multiple(sequence):
    chain = MarkovChain(sequence)
    states = chain.next("x", n=3)
    assert states[-1] == chain.state
