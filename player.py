class Player:
    def __init__(self):
        #self.name= name
        self.gestures=['rock', 'paper', 'scissors', 'lizard', 'spock']
    
   
    def choose_gesture(self):
        user_input= int(input(' Please choose a number below\nPick 1 for rock\nPick 2 for paper\nPick 3 for scissors\nPick 4 for lizard\npick 5 for spock'))
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

        

