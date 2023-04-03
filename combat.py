from type import *

class Fight(Feu, Eau, Terre, Normal):
    def __init__(self, pokemon_1, pokemon_2):
        super().__init__(self)
        self.pokemon_1 = Feu()
        self.pokemon_2 = Terre()

    def Attack_Power(self):
        if self.pokemon_1 == Feu() and self.pokemon_2 == Terre():
            (self.pokemon_1.attack - self.pokemon_2.defense) * 2

        elif self.pokemon_1 == Terre() and self.pokemon_2 == Feu():
            (self.pokemon_1.attack - self.pokemon_2.defense) * 0.5
             
    def Display_Hp(self):
        self.pokemon_1.getHp()
        self.pokemon_2.getName()

    
    
    def Check_Win(self):
        if self.pokemon_1.__hp <= 0:
            print(self.pokemon_1.__name, "tu es mort")
        
        elif self.pokemon_2.__hp <= 0:
            print(self.pokemon_2.__name, "est mort")
