import random
import sys


class RPS:
    def __init__(self):
        print("Welcome to RPS 9000!")
        # Moves for display
        self.moves: dict = {'rock': '🥌', 'paper': '📜', 'scissors': '✂️'}
        self.valid_moves: list[str] = list(self.moves.keys())

    def play_game(self):
        # Get the user input and lower() it
        user_move = input("'Rock, paper, or scissors? >> ").lower()

        if user_move == "exit":
            print("Thanks for playing")
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move..!")
            return self.play_game()

        # The AI's move
        ai_move = random.choice(self.valid_moves)
        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move: str, ai_move: str):
        # Display everything nicely
        print("-------------")
        print(f"You: {self.moves[user_move]}")
        print(f"AI: {self.moves[ai_move]}")
        print("-------------")

    def check_move(self, user_move: str, ai_move: str):
        # Game logic

        winning_conditions = {
            ('rock', 'scissors'): 'You win!',
            ('scissors', 'paper'): 'You win!',
            ('paper', 'rock'): 'You win!'
        }

        if user_move == ai_move:
            print("It is a tie!")
        elif (user_move, ai_move) in winning_conditions:
            print("You win..!")
        else:
            print('AI wins...!')


if __name__ == "__main__":
    rps = RPS()

    while True:
        rps.play_game()
