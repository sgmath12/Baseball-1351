from __future__ import annotations

from typing import Literal
from unittest import result

import pytest
from game import Game
from game_result import GameResult

@pytest.fixture
def game():
    return Game()   

def assert_illegal_argument(game, guess_number):
    with pytest.raises(TypeError):
        game.guess(guess_number)

@pytest.mark.parametrize("invalid_input", [None, "12", "1234","12s", "121"])
def test_exception_when_invalid_input(game: Game, invalid_input: None | Literal['12'] | Literal['1234'] | Literal['12s'] | Literal['121']):
    assert_illegal_argument(game, invalid_input)

def assert_matched_number(result, solved, strikes, balls):
    assert result is not None
    assert result.solved == solved
    assert result.strikes == strikes
    assert result.balls == balls

def test_return_solved_result_if_mathced_number(game: Game):
    game.question = "123"
    assert_matched_number(game.guess("123"), solved=True, strikes=3, balls=0)

def test_return_solved_result_if_unmathced_number(game: Game):
    game.question = "123"
    assert_matched_number(game.guess("456"), solved=False, strikes=0, balls=0)
