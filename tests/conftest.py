import pytest


pytest.fixture()
def mock_input_calories_by_elves():
    input_ = """1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000"""
    return input_