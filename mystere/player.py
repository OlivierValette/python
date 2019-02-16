class Player:
    
    P_LIVES = 10

    def __init__(self, firstname, lastname=""):
        self.fname = firstname
        self.lname = lastname
        self.lives = Player.P_LIVES

    def lose_live(self):
        if self.lives > 0:
            self.lives -= 1
