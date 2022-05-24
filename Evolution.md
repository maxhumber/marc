### Evolution

⚠️ **WIP**

- Evolution can be summed up in a picture:

<img alt="meme" src="/Users/max/Repos/marc/images/meme.png" width="500px">

- First written in python
  - In the before times
- Used as a teaching tool for python packaging...
- Actual code was heavily inspired by existing implementations...
  - Didn't actually stop and try to build my own from scratch.
    - Linked to a limited understanding for how chains actually worked
  - First versions were way too fancy
    - See commit:  5ea21639aba16fcfe15c5de25049d024e0bb3332
    - I was obsessed with reimplementing sklearn transformers, for some reason?
- Since March 2020 I've been spending more and more time with Swift
  - Less and less time in python...
- Needed to implement a markov chain for a client project in Swift
  - Knew I had marc (untouched since 2020)...
    - Wanted to try to write from scratch
      - Found it was way easier to just to dictionary lookup
- After swift version implemented, went back and redid python
  - Found a way simpler and more performant version
- Wanted to make the APIs match as closely as possible
  - (Especially at the call sight)
    - But be as pythonic as possible with the python
    - And as swifty as possible with the swift
- Now serve as a Rosetta Stone
  - Learning swift and writing production swift has made me a better python programmer
    - (The reverse is also true!)



**Python**

| Like 👍                              | Dislike 👎                                |
| ----------------------------------- | ---------------------------------------- |
| `defaultdict` !!                    | Clunky `setup.py` packaging              |
| `random.choice` !                   | Setting up and working with environments |
| Dictionary comprehensions + sorting | `__init__.py` and directory issues       |

**Swift**

| Like 👍                                            | Dislike 👎                                      |
| ------------------------------------------------- | ---------------------------------------------- |
| `Package.swift` and packaging in general          | Dictionary performance sucks... (surprising!!) |
| Don't have to think about environments            | Need randomness? Too bad. Go roll it yourself  |
| `XCTest` is nicer/easier than `unittest`/`pytest` | Playgrounds aren't as good as Hydrogen/Jupyter |



- *Like* 👍
  - `defaultdict` !!
  - `random.choice` inclusion in the Standard Library
  - Dictionary comprehensions + sorting
- *Dislike* 👎 
  - Clunky `setup.py` packaging
  - Setting up and working with (virtual/development) environments
  -  `__init__.py` and folder structure issues

**Swift**

- *Like* 👍
  - `Package.swift` and packaging in general
  - Natural development/environment isolation
  - `XCTest` is nicer/easier to work with than `unittest`/`pytest`
- *Dislike* 👎 
  - Dictionary insertion performance sucks... (surprising !!)
  - Need randomness? Too bad. Go roll it yourself
  - The prototyping (Playgrounds) experience isn't as good as Hydrogen/Jupyter



- How has swift made me a better developer?
  - Less reliance on third party packages
  - More intentional api design and exposure with `public`
  - More testing, because it's actually integrated
  - Functional programming 