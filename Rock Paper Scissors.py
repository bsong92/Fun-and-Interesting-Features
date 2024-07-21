import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, scissors): ").lower()
            if move in ['rock', 'paper', 'scissors']:
                return move
            else:
                print("Invalid move! Please enter 'rock', 'paper', or "
                      "'scissors.")


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move:
            return self.last_move
        else:
            return random.choice(['rock', 'paper', 'scissors'])

    def learn(self, my_move, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move_index = None

    def move(self):
        moves = ['rock', 'paper', 'scissors']
        if self.last_move_index is None:
            self.last_move_index = random.randint(0, 2)
        else:
            self.last_move_index = (self.last_move_index + 1) % 3
        return moves[self.last_move_index]


def beats(one, two):
    if one == two:
        return "Tie"
    if ((one == 'rock' and two == 'scissors') or
       (one == 'scissors' and two == 'paper') or
       (one == 'paper' and two == 'rock')):
        return "Player 1 wins"
    else:
        return "Player 2 wins"


class Game:
    def __init__(self, p1, p2, max_rounds):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
        self.max_rounds = max_rounds

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        result = beats(move1, move2)
        print(f"Results: {result}")

        if result == "Player 1 wins":
            self.score_p1 += 1
        elif result == "Player 2 wins":
            self.score_p2 += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(f"Player 1 Score: {self.score_p1} "
              f"Player 2 Score: {self.score_p2}\n")

    def play_single_round(self):
        print("Single round start!")
        self.play_round()
        print("Single round over!")

    def play_game(self):
        print("Game start!")
        for round in range(self.max_rounds):
            print(f"Round {round + 1}:")
            self.play_round()
            if self.score_p1 >= 3 or self.score_p2 >= 3:
                break
        print("Game over!")
        if self.score_p1 > self.score_p2:
            print("Player 1 wins!")
        elif self.score_p2 > self.score_p1:
            print("Player 2 wins!")
        else:
            print("It's a tie!")
        print(f"Final score: Player 1 - {self.score_p1}, "
              f"Player 2 - {self.score_p2}")


def start_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        opponent_choice = input("Choose your opponent: \nRandom / Reflect / "
                                "Cycle / Rock ").lower()
        if opponent_choice in ['random', 'reflect', 'cycle', 'rock']:
            print("You choose: ", opponent_choice)
            break
        else:
            print("Invalid choice. Please choose 'Random', "
                  "'Reflect', or 'Cycle', or 'Rock'.")

    if opponent_choice == 'random':
        opponent_player = RandomPlayer()
    elif opponent_choice == 'reflect':
        opponent_player = ReflectPlayer()
    elif opponent_choice == 'cycle':
        opponent_player = CyclePlayer()
    elif opponent_choice == 'rock':
        opponent_player = RockPlayer()

    human_player = HumanPlayer()

    while True:
        choice = input("Do you want to play a single round or "
                       "a match of several rounds? (single/match): ").lower()
        if choice == "single":
            game = Game(human_player, opponent_player, 1)
            game.play_single_round()
            break
        elif choice == "match":
            while True:
                max_rounds_input = input("Enter number of rounds for "
                                         "the match: ")
                if max_rounds_input.isdigit() and int(max_rounds_input) > 0:
                    max_rounds = int(max_rounds_input)
                    game = Game(human_player, opponent_player, max_rounds)
                    game.play_game()
                    break
                else:
                    print("Please enter a valid positive integer "
                          "for the number of rounds.")
            break
        else:
            print("Invalid choice. Please enter 'single' or 'match'.")


if __name__ == '__main__':
    start_game()
