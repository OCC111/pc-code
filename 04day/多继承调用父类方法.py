class lv():
    def __init__(self):
        self.name = "绿驹子"

    def Run(self):
        print("运货")

class ma():
    def __eat(self):
        print("吃太空椒")

    def geteat(self):
        self.__eat()

class luo(lv,ma):
    def __init__(self):
        self.name = "大马猴"
        super(luo,self).__init__()

    def getname(self):

        return "大马猴"



l = luo()
print(l.getname())
l.Run()
l.geteat()