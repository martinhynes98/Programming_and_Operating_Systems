## Task 3

import os, time, sys

C = os.fork()

if C==0:
	GC1 = os.fork()
	if GC1 !=0:
		GC2 = os.fork()
	if GC1==0:
		for i in range(5):
			time.sleep(1)
			print("GC1 is running. PPID:",os.getppid())
		print("GC1 exiting")
		sys.exit(1)
	elif GC2==0:
		for i in range(5):
			time.sleep(1)
			print("GC2 is running. PPID:",os.getppid())
		print("GC2 exiting")
		sys.exit(1)
	else:
		for i in range(20):
			time.sleep(1)
			print("C is running. PPID:",os.getppid())
else:
	for i in range(2):
		time.sleep(1)
		print("Parent is running.")

