from threading import Thread
import time

def sing():
	for i in range(10):
		print("singing!")
		time.sleep(1)

def dance():
	for i in range(10):
		print("dancing")
t1 = Thread(target=sing)
t2 = Thread(target=dance)
t1.start()
t2.start()