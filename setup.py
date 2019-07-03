from setuptools import setup
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='marc',
    version='1.0.2',
    description='Markov chains in pure python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords=[
        'markov', 'markov chain', 'transition matrix', 'list encoder'
    ],
    url='https://github.com/maxhumber/marc',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['marc'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
