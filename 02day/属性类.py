import os

class Person():
	def __init__(self,name,age,height):
		self.name = name
		self.age = age
		self.height = height
	def __str__(self):
		msg = "姓名:%s,年龄:%d,身高:%d"%(self.name,self.age,self.height)
		return msg
	def eat(self):
		print("面包")

	def sleep(self):
		print("五星级宾馆")

bing = Person('二嘎子',22,160)
print(bing)
bing1 = Person('烂菜叶',19,178)
print(bing1)
bing2 = Person('爆米花',18,170)
print(bing2)


#print(bing.age)
#print(bing.height)