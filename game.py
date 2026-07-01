from game_result import GameResult

class Game:
    def __init__(self):
        self._question = ""  # Placeholder for the actual question logic

    @property
    def question(self):
        raise AttributeError("question 속성은 읽기 전용입니다.")
    
    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)  # Placeholder for actual game result logic
        return GameResult(False, 0, 0)
      # Placeholder for actual game result logic
    def _assert_illegal_value(self, guessNumber):
        if guessNumber is None:
            raise TypeError("입력이 None입니다.")
        
        if len(guessNumber) != 3:  # Assuming the expected length is 3
            raise TypeError("입력은 3자리 숫자여야 합니다.")
        
        for number in guessNumber:
            if not ord('0') <= ord(number) <= ord('9'):
                raise TypeError("입력은 숫자여야 합니다.")
            
        if self._isDuplicateNumber(guessNumber):
            raise TypeError("중복된 숫자는 입력할 수 없습니다.")
        
    def _isDuplicateNumber(self, guessNumber):
        return len(set(guessNumber)) != 3