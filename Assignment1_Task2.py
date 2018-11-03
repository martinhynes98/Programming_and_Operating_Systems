## Task 2


import os, time

Child = os.fork()

if Child == 0:
	for i in range(30):
		time.sleep(1)
		print("This is child 1: PPID:",os.getppid())
	os._exit(0)
	
else:
	Child2 = os.fork()


if Child2==0:
	for i in range(30):
		time.sleep(1)
		print("This is child 2: PPID:",os.getppid())
	os._exit(0)
	
else:
	Child3 = os.fork()
	

if Child3 == 0:
	for i in range(30):
		time.sleep(1)
		print("This is child 3: PPID:",os.getppid())
	os._exit(0)
	
else:
	for i in range(5):
		time.sleep(1)
		print("Parent is alive.")
	print("Children becoming orphans.")

