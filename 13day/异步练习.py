from multiprocessing import Pool
import time

def download():
	for i in range(10):
		time.sleep(1)
	return "下载完成"

def notifi():
	print(arg)
p = Pool()
p.apply_async(download,callback=notifi)
p.close()
for i in range(10):
	print("看电影中")
	time.sleep(1)