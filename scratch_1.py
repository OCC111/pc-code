def w(typ):
    def w1(fun):
        def inner(*args,**kwargs):
            print("登录中...")
            return fun(*args,**kwargs)
        return inner
    return w1

@w
def yue(w1):
    print("支付中...")
    print("核实状态...")
yue()