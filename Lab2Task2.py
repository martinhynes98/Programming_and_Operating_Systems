#Martin Hynes
#16390836
#CS211 Lab 2

################
#List 1
#A: 29.6666
#B: 36.3333
#
#List 2
#A: 21.6
#B: 27.1
################

#Round Robin

#Import copy module to be used later
import copy

#Take input and convert to ints, and make it a list
durations = [int(inp) for inp in input("Enter durations, seperated by spaces: ").split()]
#Using nested lists, create index of time they reach CPU
for i in range(len(durations)):
	durations[i] = [i,durations[i]]

#Create a copy of the list object that wont change when original list is appended.
#Using general methods of creating a backup, the backup was also changed when
#Using list.append(x)
a = copy.deepcopy(durations)

#Create runningcount and wait variables
runningcount=0
waittotal=0
#For every process, calculate the wait
for process in durations:
	wait = runningcount - process[0]
	waittotal = waittotal + wait
	#If the process will end in this iteration, add duration to running count
	if process[1] <= 5:
		runningcount = runningcount + process[1]
	#Else add 5 to running count, create a new pseudo process to be run in the next iteration
	#With the duration being 5 less than before. Add to end of list
	else:
		runningcount = runningcount + 5
		x = process
		x[1] = x[1] - 5
		x[0] = runningcount
		durations.append(x)

#Calculate and print average, using length of the copy made above
#Since the parts of processes were added to durations list
av = float(waittotal)/len(a)
print("Average Wait Time:",av)

#Reset durations using deepcopy again
durations = copy.deepcopy(a)

#Create new running variables
running = 0
turntotal=0

#For every process, append the running variable with the duration of process
#To work from the end of the process rather than beginning.
for process in durations:
        #If the process will finish this iteration, add full duration to running
        #Then calculate turnaround
	if process[1] <= 5:
		running = running + process[1]
		turn = running - process[0]
		turntotal = turntotal + turn
	#Else add 5 to running, create new pseudo process with 5 less duration
	#And add to end of list
	#Turnarond is not calculated at this point, it is left until last iteration of process
	else:
		running = running + 5
		x = process
		x[1] = x[1] - 5
		durations.append(x)

#Calculate and print average, using length of deepcopy list
av = float(turntotal)/len(a)
print("Average Turnaround Time:",av)
