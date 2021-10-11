from human import Human
from ai import AI
import sys
import math

class GameBoard:
    def __init__(self):
        self.player_one = Human("player 1")
        self.player_two = None
        self.display_welcome()
       
    def run_game(self):
        self.display_welcome()
        self.game_mode()


    def display_welcome(self):
        print("Welcome to RPSLS (Rock, Paper, Scissors, Lizard, Spock)")
        print("RPSLS is just like Rock Paper Scissors, each player has to choose any one variable Rock, Paper, Scissors, Lizard or Spock.\n Once the each player has chosen there vaiable, the choicces will be revealed and compared and winner will be decleared.\n The winner will be decided by the chart below\n * Rock crushes Scissors  ---  Scissors cuts Paper --- Paper covers Rock --- Rock crushes Lizard --- Lizard poisons Spock \n Spock smashes Scissors --- Scissors decapitates Lizard --- Lizard eats Paper --- Paper disproves Spock --- Spock vaporizes Rock")
       

    def game_mode(self):
        game_mode = int(input("1 - To play against a another human \n2 - To Play against the computer\n"))
        
        number_of_games = self.number_of_games()
        player_one_name = input('\nPlease enter your name: ')
        if game_mode == 1: 
            player_two_name = input('\nPlease enter your name: ')
            self.player_two = Human(player_two_name)
            self.play_game(number_of_games,player_one_name)
            
        elif game_mode == 2:
           self.player_two = AI("Iron Man")
           self.play_game(number_of_games,player_one_name)
           
        else:
            print("Please only pick 1 or 2!")
            self.game_mode()
   
    def number_of_games(self):
        number_of_games = int(input("\n Please choose number of games up to 20: \n"))
        amount_to_win = math.floor(number_of_games / 2) + 1 

        return amount_to_win

    def play_game(self,number_of_games,player_one_name):
        
        player_1_score = 0 
        player_2_score = 0 
        game_over = False
        choice1 = ""
        choice2 = ""
        player_2_name = self.player_two.name
        
        while game_over == False:
            print(f'\n{player_one_name}, It is your turn.')
            choice1 = self.player_one.choose_gesture()
            print(f'\n{player_2_name}, It is your turn.')
            choice2 = self.player_two.choose_gesture()
            print(f'\n{player_one_name} has {choice1} VS {player_2_name} has {choice2}')
            winner = self.determine_winner(choice1,choice2)
            if winner == choice1:
                player_1_score += 1
                print(f"\n {player_one_name} has a score of {player_1_score}")
                print(f" {player_2_name} has a score of {player_2_score}")

            elif winner == choice2:
                player_2_score += 1
                print(f"\n {player_one_name} has a score of {player_1_score}")
                print(f" {player_2_name} has a score of {player_2_score}")
                

            if player_1_score == number_of_games:
                self.display_winner(player_one_name)
                game_over = True
            elif player_2_score == number_of_games:
                self.display_winner(player_2_name)
                game_over = True
                
            
    def determine_winner(self, choice1, choice2):
        if choice1 == 'rock' and choice2 == 'scissors':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'scissors' and choice2 == 'paper':
             print(f"{choice1} beats {choice2}")
             return choice1
        elif choice1 == 'paper' and choice2== 'rock':
             print(f"{choice1} beats {choice2}")
             return choice1
        elif choice1 == 'rock' and choice2== 'lizard':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'lizard' and choice2== 'spock':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'spock' and choice2== 'scissors':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'scissors' and choice2== 'lizard':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'lizard' and choice2== 'paper':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'paper' and choice2== 'spock':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice1 == 'spock' and choice2== 'rock':
            print(f"{choice1} beats {choice2}")
            return choice1
        elif choice2 == 'rock' and choice1 == 'scissors':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'scissors' and choice1== 'paper':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'paper' and choice1== 'rock':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'rock' and choice1== 'lizard':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'lizard' and choice1== 'spock':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'spock' and choice1== 'scissors':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'scissors' and choice1== 'lizard':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'lizard' and choice1== 'paper':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'paper' and choice1== 'spock':
            print(f"{choice2} beats {choice1}")
            return choice2
        elif choice2 == 'spock' and choice1== 'rock':
            print(f"{choice2} beats {choice1}")
            return choice2
        else:
            print(f'Its a draw! You both choose {choice1}')
            


    def display_winner(self, player):
        print(f"\nCongrats {player} you have won the game!")
        answer = input('\nWould you like to play again?\n 1- Play Again\n 2- End Game\n Enter Choice: ')
        if answer == "1":
             self.run_game()
        else:
            sys.exit()
        
     