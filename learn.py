class Student():
    def __init__(self):
        self.count = 0

class B():
    def handle(self,eat):
        self.eat = eat
        return "小龙虾"
class A(B):
    pass

xm = A()
xm.handle("小龙虾")
print(xm.handle("小龙虾"))