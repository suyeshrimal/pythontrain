class GrandFather:
    house="luxury House"
    def __init__(self) -> None:
        print("GrandFather")
    
    def get_house(self):
        return self.house
    

class GrandMother:
    def __init__(self) -> None:
        print("Grandmother")
    jewels="goldy"

class Father(GrandFather,GrandMother):
    car="BMW"

    def get_house(self):
        print(super().get_house())
        return "jhan ramro ghar"
    

class Son(Father):
    game="PS5"
father=Father()

print(father.get_house())
# son=Son()
# print(father.car)
# print(father.house)
# print(father.jewels)
# print(son.car)
# print(son.game)
# print(son.house)
# print(son.jewels)
# print(isinstance(son,object))
#do example of inheritance
