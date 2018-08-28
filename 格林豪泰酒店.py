import re
# 验证手机号是否正确
phone_pat = re.compile(r'^1[3-9]\d{9}$')
name_pat = re.compile(r'^Simle[A-Z]{6}$')
class Student():
    def __init__(self):
        self.list1 = []

    def menu(self):
        while True:
            user = int(input("北京格林豪泰酒店\n1.登记保存\n2.退出\n输入:"))
            if user == 1:
                #验证手机号
                phone = input('请输入您的手机号:')
                name = input("请输入您的姓名:")
                res1 = re.search(name_pat, name)

                res = re.search(phone_pat,phone)
                if res and res1:
                    continue
                else:
                    print("格式错误,重新输入")

                self.list1.append(phone)
                self.list1.append(name)
                for i in self.list1:
                    str(i)
                    print(" ")
                    f = open("2.txt", "a")
                    f.write(i)
                    f.close()
                    print("保存成功")

            elif user == 3:
                print("感谢您来格林豪泰!")
                break

xm = Student()
xm.menu()