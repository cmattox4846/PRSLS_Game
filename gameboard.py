from human import Human
from ai import AI


class GameBoard:
    def __init__(self):
        pass

    def display_welcome(self):
        print("Welcome to RPSLS (Rock, Paper, Scissors, Lizard, Spock)")
        print("RPSLS is just like Rock Paper Scissors, each player has to choose any one variable Rock, Paper, Scissors, Lizard or Spock.\n Once the each player has chosen there vaiable, the choicces will be revealed and compared and winner will be decleared.\n The winneer will be decided by the chart below\n * Rock crushes Scissors  ---  Scissors cuts Paper --- Paper covers Rock --- Rock crushes Lizard --- Lizard poisons Spock \n Spock smashes Scissors --- Scissors decapitates Lizard --- Lizard eats Paper --- Paper disproves Spock --- Spock vaporizes Rock")

    def game_mode(self):
        game_mode = int(input("1 - To play against a another human \n 2 - To Play against the computer"))
        if game_mode == 1: 
            self.multiplayer_play_game()
        elif game_mode == 2:
           self.single_play_game()
        else:
            print("Please only pick 1 or 2!")
            game_mode()
        

    def single_play_game(self):
        player_1_score = 0 
        player_2_score = 0 
        game_over = False
        choice1 = ""
        choice2 = ""
        while game_over == False:
            choice1 = self.human_turn()
            choice2 = self.ai_turn()
            winner = self.determine_winner(choice1,choice2)
            if winner == 1:
                player_1_score += 1
            elif winner == 2:
                player_2_score += 1
            if player_1_score == 2 or player_2_score == 2:
                game_over = True
            
    def determine_winner(self, choice1, choice2):
        if choice1 == 'rock' and choice2 == 'scissors':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'scissors' and choice2 == 'paper':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'paper' and choice2== 'rock':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'rock' and choice2== 'lizard':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'lizard' and choice2== 'spock':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'spock' and choice2== 'scissors':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'scissors' and choice2== 'lizard':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'lizard' and choice2== 'paper':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'paper' and choice2== 'spock':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice1 == 'spock' and choice2== 'rock':
            winner = print(f"{choice1} beats {choice2}")
            return 1
        elif choice2 == 'rock' and choice1 == 'scissors':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'scissors' and choice1== 'paper':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'paper' and choice1== 'rock':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'rock' and choice1== 'lizard':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'lizard' and choice1== 'spock':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'spock' and choice1== 'scissors':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'scissors' and choice1== 'lizard':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'lizard' and choice1== 'paper':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'paper' and choice1== 'spock':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        elif choice2 == 'spock' and choice1== 'rock':
            winner = print(f"{choice2} beats {choice1}")
            return 2
        
        

    def multiplayer_play_game(self):
        

        player_1_score = 0 
        player_2_score = 0 
        game_over = False
        choice1 = ""
        choice2 = ""
        while game_over == False:
            choice1 = self.human_turn()
            choice2 = self.ai_turn()
            if 


    def human_turn(self):
        name_input = input('Please enter your name: ')
        player1 = Human(name_input)
        gesture_choice = player1.choose_gesture()
        return gesture_choice

    def ai_turn(self):
        player2 = AI("Iron Man")
        guesture_choice = player2.choose_gesture()
        return guesture_choice

    

    def display_winner(self):
        pass
