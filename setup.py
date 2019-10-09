from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='marc',
    version='2.0',
    description='marc is a small, but flexible Markov chain generator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ],
    keywords=[
        'markov', 'markov chain', 'transition matrix', 'list encoder'
    ],
    url='https://github.com/maxhumber/marc',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    py_modules=['marc'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
