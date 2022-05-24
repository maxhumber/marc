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
- What I think about each
  - Good Python:
    - `Random.choice`
    - Dictionary insertion is way faster? Surprising??
      - COW stuff in swift
    - Ability to sort dictionaries
    - default dictionary
    - dictionary comprehensions
  - Bad python:
    - setup.py is just worse...
    - Dev environment (vent) is a buzzkill
    - Issues with jupyter/atom + pytest (still unresolved)
    - Folder structure issues, __init__.py

  - Good swift:
    - Packaging is way easier
    - Dev environment is something you don't even have to think about
    - Types! (I know python has 'em but they're really not the same at all...)
    - Generics
    - XCTest sitting right beside the code
  - Bad swift: 
    - Playgrounds are slow...
    - Adding resources to playgrounds is harder
    - No random? Had to roll my own (not bad, but a little surprising tbh)
- How has swift made me a better developer?
  - Less reliance on third party packages
  - More intentional api design and exposure with `public`
  - More testing, because it's actually integrated
  - Functional programming 