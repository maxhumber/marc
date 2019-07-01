<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/marc/master/images/logo.png" width="500px" alt="marc">
</h3>
<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img alt="MIT" src="https://img.shields.io/github/license/maxhumber/marc.svg"></a>
  <a href="https://travis-ci.org/maxhumber/marc"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="PyPI" src="https://img.shields.io/pypi/v/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="Downloads" src="https://img.shields.io/pypi/dw/marc.svg"></a>
</p>


### About

marc is a "proof-of-concept" package that demonstrates the possibility of building Markov chains in pure python.

### Usage

```python
from marc import MarkovChain

chain = [
    'Rock', 'Rock', 'Paper', 'Rock', 'Scissors',
    'Paper', 'Paper', 'Paper', 'Scissors', 'Rock',
    'Scissors', 'Scissors', 'Paper', 'Rock', 'Rock',
    'Rock', 'Rock', 'Paper', 'Rock', 'Rock'
]

mc = MarkovChain(chain)

mc.next_state('Rock')
# 'Rock'

mc.generate_states('Paper', n=5)
# ['Scissors', 'Paper', 'Rock', 'Paper', 'Scissors']

mc.next_state('Scissors')
# 'Paper'

```
### Install

`pip install marc`
