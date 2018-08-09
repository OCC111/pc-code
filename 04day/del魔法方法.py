class Dog():
    def __init__(self,name):
        self.name = name

    def __str__(self):
        msg = "狗的名字是%s"%self.name
        return msg
    def __del__(self):
        print("分手吧")


D = Dog("儿哈")
D1 = D

del D
del D1

