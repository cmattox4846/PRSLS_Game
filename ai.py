from player import Player
import random

class AI(Player):
    def __init__(self, name):
        self.name = name
        super().__init__(name)
        
    
    def choose_gesture(self):
        ai_input = random.randint(1, 5)
        if ai_input == 1:
            return 'rock'
        elif ai_input== 2:
            return 'paper'
        elif ai_input== 3:
            return 'scissors'
        elif ai_input== 4:
            return 'lizard'
        elif ai_input== 5:
            return 'spock'
     
