from pokemon import *

class Feu(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.setName("Salamèche")   
        self.setHp(110)  
        self.attack = 50
        self.defense = 45
        self.type = "feu"

class Eau(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.setName("Carapuce")   
        self.setHp(80)  
        self.attack = 65
        self.defense = 35
        self.type = "eau"

class Terre(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.setName("Racaillou")   
        self.setHp(90)  
        self.attack = 60
        self.defense = 25
        self.type = "terre"

class Normal(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.setName("Rattata")   
        self.setHp(100)  
        self.attack = 45
        self.defense = 55
        self.type = "feu"

