#coding=utf-8
import random
class Student():
    def __init__(self,name):
        self.name = name
        self.list1 = ["we","OMG","CG","GT"]
    def menu(self):

        while True:
            for i in self.list1:

                pc = random.sample(i,2)
                f1 = open("1.txt", "a")
                for j in i:
                    str(j)
                    print(" ")
                f1.write(j)
                f1.close()



xm = Student("小名")
xm.menu()

