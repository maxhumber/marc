from setuptools import setup
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='marc',
    version='0.1.1',
    description='Simple Markov Chains in Pure Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords=[
        'markov', 'markov chain', 'transition matrix'
    ],
    url='https://github.com/maxhumber/marc',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['marc'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
