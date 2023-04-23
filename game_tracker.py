from round import Round
from scoreboard import Scoreboard

class GameTracker:
    def __init__(self):
        self.scoreboard = Scoreboard()
    
    def start_game(self):
        print('\nWELCOME TO ROCK & STONE, PAPER, SCISSORS!\n')

        print('ROCK & STONE beats SCISSORS')
        print('SCISSORS beats PAPER')
        print('PAPER beats ROCK & STONE\n')

        self.total_rounds = int(input('How many rounds would you like to play?   ENTER A NUMBER: '))

        print(f'PLAYING {self.total_rounds} ROUNDS!')

        self._start_rounds()
    
    def end_game(self):
        self.scoreboard.give_winner()
        print('Thank you for playing! Rock & Stone, Brother!\n')

    def _start_rounds(self):
        for round_number in range(1, self.total_rounds + 1):
            print(f'ROUND {round_number} OF {self.total_rounds}')
            print('CHOICES:   1. ROCK & STONE   2. PAPER   3. SCISSORS')
            
            round_in_play = Round(round_number)

            self.scoreboard.evaluate_round(round_in_play)

            print(f'\nEND OF ROUND: {round_number} - USER: {self.scoreboard.user_score} | {self.scoreboard.computer_score} COMPUTER\n\n')

