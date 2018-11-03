#import all necessary modules
import os,time,sys

##Create First pipe object
r,w = os.pipe()
r = os.fdopen(r,'r',0)
w = os.fdopen(w,'w',0)
##Create second pipe object
r1,w1 = os.pipe()
r1 = os.fdopen(r1,'r',0)
w1 = os.fdopen(w1,'w',0)
##Fork for first time
child1 = os.fork()
##If it is the parent process:
if child1:
        ##Create second child process
	child2 = os.fork()
	#os.wait was not working for some reason. It claimed there were no child processes, even though I had both
	#child processes returning the correct ppid.
	#Instead I used time.sleep, which is not a great substitute, as the reversed string is not given until the timer is up,
	#And if the timer is up before the input is given, it will lead to the program not working right.
	time.sleep(10)

#If it is the child1 process, take input from user, and write it.
if child1==0:
	st=input("Enter a string: ")
	r.close()
	print "Child1 writing inputted string."
	w.write(st)
	w.close()

#If it is child 2, read the input from the first child
elif child2 == 0:
	w.close()
	print "Child2 reading inputted string."
	text = r.read()
	#Invert said input
	text1= text[::-1]
	r1.close()
	print "Child2 writing reversed string."
	#Write inverted input using second pipe
	w1.write(text1)
	w1.close()
	#Exit child2 process
	sys.exit(1)

#If it is the first child
if child1==0:
        #Read inverted input from second pipe
	print "Child 1 reading reversed string."
	w1.close()
	string=r1.read()
	#Print result
	print("Text: "+string)
	#Exit child1 process
	sys.exit(1)
