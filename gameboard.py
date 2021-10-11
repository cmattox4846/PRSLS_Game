from human import Human
from ai import AI
import sys

class GameBoard:
    def __init__(self):
       self.display_welcome()
       

    def display_welcome(self):
        print("Welcome to RPSLS (Rock, Paper, Scissors, Lizard, Spock)")
        print("RPSLS is just like Rock Paper Scissors, each player has to choose any one variable Rock, Paper, Scissors, Lizard or Spock.\n Once the each player has chosen there vaiable, the choicces will be revealed and compared and winner will be decleared.\n The winneer will be decided by the chart below\n * Rock crushes Scissors  ---  Scissors cuts Paper --- Paper covers Rock --- Rock crushes Lizard --- Lizard poisons Spock \n Spock smashes Scissors --- Scissors decapitates Lizard --- Lizard eats Paper --- Paper disproves Spock --- Spock vaporizes Rock")
        self.game_mode()

    def game_mode(self):
        game_mode = int(input("1 - To play against a another human \n2 - To Play against the computer\n"))
        if game_mode == 1: 
            self.multiplayer_play_game()
        elif game_mode == 2:
           self.single_play_game()
        else:
            print("Please only pick 1 or 2!")
            self.game_mode()
        

    def single_play_game(self):
        name_input = input('Please enter your name: ')
        player1 = Human(name_input)
        
        player_1_score = 0 
        player_2_score = 0 
        game_over = False
        choice1 = ""
        choice2 = ""
        while game_over == False:
            choice1 = self.human_turn(player1)
            choice2 = self.ai_turn()
            print(f'Player 1 has {choice1} VS Player 2 has {choice2}')
            winner = self.determine_winner(choice1,choice2)
            if winner == 1:
                player_1_score += 1
                print(f" Player 1 has a score of {player_1_score}")
                print(f" Player 2 has a score of {player_2_score}")

            elif winner == 2:
                player_2_score += 1
                print(f" Player 1 has a score of {player_1_score}")
                print(f" Player 2 has a score of {player_2_score}")
                

            if player_1_score == 2:
                self.display_winner(name_input)
                game_over = True
            elif player_2_score == 2:
                self.display_winner("Iron Man")
                
            
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
            winner = print(f"{choice2} beats {choice1}")
            return 2
        else:
            winner = print(f'Its a draw! You both choose {choice1}')

         
        
        

    def multiplayer_play_game(self):
        

        player_1_score = 0 
        player_2_score = 0 
       
        
        
        name_input = input('Please enter your name: ')
        player1 = Human(name_input)
        name_input = input('Please enter your name: ')
        player2 = Human(name_input)




        while player_1_score <= 2 or player_2_score <= 2:
            print(f'{player1.name}, It is your turn.')
            player_one_choice= self.human_turn(player1)
            print(f'{player2.name}, It is your turn.')
            player_two_choice= self.human_turn(player2)
            winner= self.determine_winner(player_one_choice, player_two_choice)
            if winner == player_one_choice:
                player_1_score += 1
            elif winner == player_two_choice:
                player_2_score += 1

            if player_1_score == 2:
                self.display_winner(player1)
            elif player_2_score == 2:
                self.display_winner(player2)

        

            
            


    def human_turn(self, player):
       
        gesture_choice = player.choose_gesture()
        print(f'You chose {player.choose_gesture}')
        return gesture_choice

    def ai_turn(self):
        player2 = AI("Iron Man")
        guesture_choice = player2.choose_gesture()
        return guesture_choice

    

    def display_winner(self, player):
        print(f"Congrats {player.name} you have won the game!")
        answer = input('Would you like to play again?\n 1- Play Again\n 2- End Game\n Enter Choice: ')
        if answer == "1":
             self.display_welcome()
        else:
            sys.exit()
        
     