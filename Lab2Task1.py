#Martin Hynes
#16390836
#CS211 Lab 2

################
#List 1
#A: 41.88
#B: 21.55
#
#List 2
#A: 10.4
#B: 15.9
################

#Shortest Task First

#Create list from input, make them ints
durations = [int(inp) for inp in input("Enter durations, seperated by spaces: ").split()]
#Create nested lists to keep track of original position in list
#a.k.a. the time they reach the CPU
for num in range(len(durations)):
	durations[num] = [num,durations[num]]

#Bubble Sort algorithm to sort into ascending order of duration
for i in range(len(durations)-1):
	for j in range(1,len(durations)-i):
		if durations[j-1][1] > durations[j][1]:
			temp = durations[j]
			durations[j] = durations[j-1]
			durations[j-1] = temp

#2 variables needed, running count, and the total wait time
runningcount = 0
waittotal = 0
#for each process, find the wait time, and add it to waittotal
#also append the runningcount by adding the run time
for process in durations:
	wait = runningcount - process[0]
	waittotal = waittotal + wait
	runningcount = runningcount + process[1]
#without specifying float, ubuntu was flooring the result
#Average found and printed.
av = float(waittotal)/(len(durations))
print("Average Waiting Time:",av)

#Almost exact same process as above
#New variable names, same concept
running = 0 
turntotal = 0
#For each process, append running time first, to find the end of the process
#Rather than the beginning like before
for process in durations:
	running = running + process[1]
	turn = running - process[0]
	turntotal = turntotal+turn
#Find and Print the average
average = float(turntotal)/len(durations)
print("Average Turnaround Time:",average)
