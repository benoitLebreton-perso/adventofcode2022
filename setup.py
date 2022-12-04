from setuptools import find_packages, setup


with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="adventofcode",
    version="1.0",
    description="Python code challenge : advent of code",
    author="Quantmetry",
    author_email="",
    install_requires=required,
    packages=find_packages(),
)
