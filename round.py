import random
from loses_to import loses_to, result

class Round:
    def __init__(self, round_number) -> None:
        self.round_number = round_number
        self._play()

    def _play(self):
        self.computer_move = random.randint(1, 3)
        self.user_move = int(input('Enter 1, 2, or 3:'))

    def is_user_winner(self):
        print(f'You chose {self.user_move} and the computer chose {self.computer_move}!\n')

        if(self.user_move == loses_to[self.computer_move]):
            return result["lose"]
        elif(self.computer_move == loses_to[self.user_move]):
            return result["win"]
        else:
            return result["tie"]

    