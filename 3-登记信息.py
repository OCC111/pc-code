class Student():
    def __init__(self,name):
        self.list1 = []
        self.name = name

    def menu(self):
        global name
        while True:
            user = input("------------\n北京国际大酒店\n1.录入信息\n2.退出\n------------\n选择:")
            if user == "1":
                name = input("输入姓名:")
                self.list1.append(name)
                for i in self.list1:
                    str(i)
                    print(" ")
                    f = open("2.txt","a")
                    f.write(i)
                    print("已成功登记用户:%s"%self.list1)
                    f.close()
            else:
                print("谢谢光临")
                break

xm = Student("哈哈")
xm.menu()
