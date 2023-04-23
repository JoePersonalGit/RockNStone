from round import Round

class Scoreboard:
    def __init__(self):
        self.user_score = 0
        self.computer_score = 0

    def evaluate_round(self, round:Round):
        result = round.is_user_winner()
        if result == 0:
            print(f'YOU TIED ROUND {round.round_number}!')
        if result == 1:
            print(f'YOU WON ROUND {round.round_number}!')
            self.user_score += 1
        if result == 2:
            print(f'YOU LOST ROUND {round.round_number}!')
            self.computer_score += 1
    
    def give_winner(self):
        print('FINAL RESULT:\n')
        if self.user_score > self.computer_score:
            print('YOU WON THE GAME!\n\n')
        elif self.user_score < self.computer_score:
            print('YOU LOST THE GAME!\n\n')
        elif self.user_score == self.computer_score:
            print('YOU TIED THE GAME!\n\n')
    