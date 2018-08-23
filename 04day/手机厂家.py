class Phone():
    count = 0
    def __init__(self,color,types):
        self.color = color
        self.types = types
        Phone.count+=1
    def __str__(self):
        msg = "品牌:%s,颜色:%s"%(self.types,self.color)
        return msg
    def chong(self):
        print("充电")
    def play(self):
        print("办公")

xm = Phone("红色","MI mix")
xm2 = Phone("红色","MI mix2")
xm3 = Phone("红色","MI mix3")

print(xm)
xm.chong()
xm.play()
print(Phone.count)






