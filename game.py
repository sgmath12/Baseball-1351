class Game:
    def guess(self, guess_number):
        self._assert_illegal_value(guess_number)

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