<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/marc/master/marc.png" width="500px" alt="marc">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/marc/blob/master/setup.py"><img alt="Dependencies" src="https://img.shields.io/badge/dependencies-zero-brightgreen"></a>
  <a href="https://travis-ci.org/maxhumber/marc"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/marc.svg"></a>
  <a href="https://pypi.python.org/pypi/marc"><img alt="PyPI" src="https://img.shields.io/pypi/v/marc.svg"></a>
  <a href="https://pepy.tech/project/marc"><img alt="Downloads" src="https://pepy.tech/badge/marc"></a>
</p>


#### About

marc (<I>**mar**kov **c**hain</I>) is a small, but flexible Markov chain generator.



#### Usage

marc is easy to use. To build a `MarkovChain` pass the object a sequence of items:

```python
from marc import MarkovChain

sequence = [
    'Rock', 'Rock', 'Rock', 'Paper', 'Rock', 'Scissors',
    'Paper', 'Paper', 'Scissors', 'Rock', 'Scissors',
    'Scissors', 'Paper', 'Scissors', 'Rock', 'Rock', 'Rock',
    'Paper', 'Scissors', 'Scissors', 'Scissors', 'Rock'
]

chain = MarkovChain(sequence)
```

The learned transition matrix can be accessed through the `matrix` attribute:

```python
print(chain.matrix)
# [[0.5, 0.25, 0.25], [0.2, 0.2, 0.6], [0.375, 0.25, 0.375]]
```

Though, the output is perhaps better viewed as a pandas `DataFrame`:

```python
import pandas as pd

df = pd.DataFrame(
    chain.matrix,
    index=chain.encoder.index_,
    columns=chain.encoder.index_
)

print(df)
#            Rock  Paper  Scissors
# Rock      0.500   0.25     0.250
# Paper     0.200   0.20     0.600
# Scissors  0.375   0.25     0.375
```

Use the `next` method to generate the next state (seeded or unseeded):

```python
chain.next('Rock')
# 'Rock'

chain.next()
# Paper
```

The `next` method can also generate multiple states with the `n` argument:

```python
chain.next('Paper', n=5)
# ['Scissors', 'Paper', 'Rock', 'Paper', 'Scissors']
```

`MarkovChain` objects are iterable. This means that they can be passed directly to the  `next` function:

```python
next(chain)
# 'Scissors'

next(chain)
# Rock
```



#### Example

A fully worked example of marc in action (block text provided by [quote](https://github.com/maxhumber/quote)):

```python
import random
import re
from quote import quote
from marc import MarkovChain

quotes = quote('shakespeare', 250)
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

