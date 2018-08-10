class lv():
    def eat(self):
        print("驴说：你可以吃草")

class ma():
    def __run(self):
        print("骏马说：你能日行千里")
    def getrun(self):
        self.__run()

class luo(lv,ma):
    pass

l = luo()
l.eat()
l.getrun()