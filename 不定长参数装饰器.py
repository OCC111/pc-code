def w1(fun):
    def inner(*args,**kwargs):
        print("登陆中")
        return fun(*args,**kwargs)#不定长参数
    return inner

@w1
def test(arg): #等同 test =
    #  w1(test)
    print("验证中")
    print(arg)
    def test1(arg):
        print(arg)
        print("退出系统成功")
    test1("谢谢使用")
test("支付中")
