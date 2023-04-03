class Pokemon:
    def __init__(self, name):
        self.__name = name
        self.__hp = 100
        self.level = 1
        self.attack = 0
        self.defense = 0
        self.type = ""

    def setName(self, name):
        self.__name = name

    def getName(self):
        print(self.__name)
        return self.__name
    
    def setHp(self, hp):
        self.__hp = hp

    def getHp(self):
        print(self.__hp)
        return self.__hp
    
    
    
    