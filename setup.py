from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="marc",
    version="3.0rc1",
    url="https://github.com/maxhumber/marc",
    description="Markov chain generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Max Humber",
    author_email="max.humber@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    package_dir={"": "python/src"},
    packages=find_packages(where="src"),
    extras_require={
        "dev": [
            "black>=22.3.0",
        ],
    },
    python_requires=">=3.9",
    setup_requires=["setuptools>=62.1.0"],
)
