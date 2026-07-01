import pytest
from game import Game

@pytest.fixture
def game():
    return Game()   

def assert_illegal_argument(game, guessNumber):
    try:
       game.guess(guessNumber)
       pytest.fail("Expected TypeError for input length less than 3")
    except:
        pass

def test_exception_when_invalid_input(game):
    assert_illegal_argument(game, None)
    assert_illegal_argument(game, "12")  # Input length is 2, which is less than expected
    assert_illegal_argument(game, "1234")  # Input length is 4, which is more than expected