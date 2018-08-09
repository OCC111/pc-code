class Animal(object):
    def __init__(self,name):
        self.__name = name

    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def __eat(self):
        print("吃吃吃")
    def geteat(self):
        self.__eat()
class Cat(Animal):
    pass

class Dog(Animal):
    pass

class People(Animal):
    pass



bs = Cat("波斯猫")
bs.getname()
print(bs.getname())
bs.geteat()
print(bs.geteat())

print("")

wc = Dog("旺财")
wc.getname()
print(wc.getname())
wc.geteat()
print(wc.geteat())

print("")



b = People("冰冰")
b.getname()
print(b.getname())
b.geteat()
print(b.geteat())