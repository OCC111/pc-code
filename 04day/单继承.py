class lv():
    def eat(self):
        print("吃草")

class ma():
    def __run(self):
        print("日行千里")
    def getrun(self):
        self.__run()
class luo(lv,ma):
    pass

l = luo()

l.eat()

l.getrun()