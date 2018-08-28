import random

l1 = []

def funs():
    i = 0
    for pc in range(10):
        pc=random.randrange(1,100,1)
        l1.append(pc)
        l2 = sorted(set(l1),key=l1.index)
        l2.sort()

        a = str(l2)
        print(" ")
        print(" ")
        print(" ")
        f = open("2.txt","a")
        f.write(a)
        f.close()
        print(l2)

funs()