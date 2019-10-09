<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/marc/master/marc.png" width="500px" alt="marc">
</h3>
<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img alt="MIT" src="https://img.shields.io/github/license/maxhumber/marc.svg"></a>
  <a href="https://travis-ci.org/maxhumber/marc"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="PyPI" src="https://img.shields.io/pypi/v/marc.svg"></a>
  <a href="https://pepy.tech/project/marc"><img alt="Downloads" src="https://pepy.tech/badge/marc"></a>
</p>


#### About

marc (<I>**mar**kov **c**hain</I>) is a small, but flexible Markov chain generator.



#### Usage

marc is easy to use. To instantiate a `MarkovChain` object pass the constructor a collection of items:

```python
from marc import MarkovChain

sequence = [
    'Rock', 'Rock', 'Paper', 'Rock', 'Scissors',
    'Paper', 'Paper', 'Paper', 'Scissors', 'Rock',
    'Scissors', 'Scissors', 'Paper', 'Rock', 'Rock',
    'Rock', 'Rock', 'Paper', 'Rock', 'Rock'
]

chain = MarkovChain(sequence)
```

Use the `next` method to generate the next state from the chain:

```python
chain.next('Rock')
# 'Rock'

chain.next('Paper', n=5)
# ['Scissors', 'Paper', 'Rock', 'Paper', 'Scissors']

chain.next()
# Paper
```

Or, call the `next` function directly on top of the object:

```python
next(chain)
# 'Scissors'

next(chain)
# Rock
```



#### Example

Here's a fully worked example of using marc with a block of text (built with [quote](https://github.com/maxhumber/quote)):

```python
import random
import re
from quote import search # pip install quote
from marc import MarkovChain

quotes = search('shakespeare', 250)
print(quotes[0])

# {'author': 'William Shakespeare',
#  'book': 'As You Like It',
#  'quote': 'The fool doth think he is wise, but the wise man knows himself to be a fool.'}

text = '\n'.join([q['quote'] for q in quotes])
text = text.lower()

tokens = re.findall(r"[\w']+|[.,!?;]", text)
tokens[:5]

# ['the', 'fool', 'doth', 'think', 'he']

chain = MarkovChain(tokens)

def generate_sentences(chain, n=2, length=(10, 20)):
    for _ in range(n):
        l = random.randint(length[0], length[1])
        nonsense = ' '.join(chain.next(n=l))
        print(nonsense)

generate_sentences(chain)

# and unless by some are fascinated by the hour upon the wind faithful
# those that hath had a very much as flaws go
```



#### Install

```
pip install -U marc
```
