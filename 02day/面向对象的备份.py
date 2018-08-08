class copys():
	def paste(self):
		name = input("输入要备份的文件名字:")
		f = open(name,"r")
		while True:
			content = f.read(1024)
			if len(content) == 0:
				break
		name1 = input("输入备份后的名字:")
		f1 = open(name1,"w")
		f1.write(content)

		f.close()
		f1.close()

C = copys()
C.paste()