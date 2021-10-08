
from player import Player


class Human(Player):
    def __init__(self, name):
        self.name= name
        super().__init__(name)
        
    
    def choose_gesture(self):
        user_input= int(input(' Please choose a number below\nPick 1 for rock\npick 2 for paper\n pick 3 for scissors\npick 4 for lizard\npick 5 for spock\n'))
        if user_input == 1:
            return 'rock'
        elif user_input== 2:
            return 'paper'
        elif user_input== 3:
            return 'scissors'
        elif user_input== 4:
            return 'lizard'
        elif user_input== 5:
            return 'spock'
        else:
            print('choose valid number')
            self.choose_gesture()

        