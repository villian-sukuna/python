class Dad:
    def __init__(self, house):
        self.__house = house

    def Get_House(self):
        return self.__house

    def introduce(self):
        print("I am Dad")


class Mom:
    def __init__(self, talent):
        self.talent = talent

    def cooking(self):
        print("Mom is Cooking")


class Son(Dad, Mom):
    def __init__(self, house, talent, name):
        Dad.__init__(self, house)
        Mom.__init__(self, talent)
        self.name = name

    def introduce(self):
        print("I am Son")
        print("Name:", self.name)
        print("House:", self.Get_House())
        print("Talent:", self.talent)


s1 = Son("Chennai", "Cooking", "JB")
s1.introduce()