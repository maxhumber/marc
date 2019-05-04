import pytest
from marc import ListEncoder, chain_to_matrix

@pytest.fixture
def throws():
    return [
        'rock', 'rock', 'paper', 'scissors', 'paper', 'rock', 'rock',
        'scissors', 'paper', 'paper', 'paper', 'rock', 'paper', 'rock'
    ]

# throws = throws()

def test_list_encoder(throws):
    encoder = ListEncoder()
    encoder.fit(throws)
    e = encoder.transform(['rock', 'paper', 'scissors'])
    d = encoder.inverse_transform(e)
    assert e == d



##
