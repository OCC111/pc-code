import time
def w1(fun):
    def inner(*args,**kwargs):
        print("登陆中...")
        return fun(*args,**kwargs)
    return inner

@w1
def yue(arg):
    time.sleep(1)
    print("支付中...")
    time.sleep(1)
    print(arg)
    time.sleep(1)
yue("已成功交易,返回初始界面!")
time.sleep(1)
print("-----------------------------------")
time.sleep(1)

@w1
def yue1(arg):
    time.sleep(1)
    print("正在进行最后的结算...")
    time.sleep(1)
    print(arg)
yue1("感谢光临本网站,下次再见!")
