<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/marc/master/marc.png" width="500px" alt="marc">
</h3>
<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img alt="MIT" src="https://img.shields.io/github/license/maxhumber/marc.svg"></a>
  <a href="https://travis-ci.org/maxhumber/marc"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="PyPI" src="https://img.shields.io/pypi/v/marc.svg"></a>
  <a href="https://pepy.tech/project/marc"><img alt="Downloads" src="https://pepy.tech/badge/marc"></a>
</p>


### About

marc (<I>**mar**kov **c**hain</I>) is a small, but flexible Markov chain generator.

### Usage

marc is easy to use:

```python
from marc import MarkovChain

chain = [
    'Rock', 'Rock', 'Paper', 'Rock', 'Scissors',
    'Paper', 'Paper', 'Paper', 'Scissors', 'Rock',
    'Scissors', 'Scissors', 'Paper', 'Rock', 'Rock',
    'Rock', 'Rock', 'Paper', 'Rock', 'Rock'
]

mc = MarkovChain(chain)

mc.next('Rock')
# 'Rock'

mc.next('Paper', n=5)
# ['Scissors', 'Paper', 'Rock', 'Paper', 'Scissors']

mc.next('Scissors')
# 'Paper'

mc.next()
# 'Scissors'
```

### Install

```
pip install -U marc
```
