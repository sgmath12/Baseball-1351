class Game:
    def guess(self, guessNumber):
        if guessNumber is None:
            raise TypeError()
        if len(guessNumber) != 3:  # Assuming the expected length is 3
            raise TypeError()