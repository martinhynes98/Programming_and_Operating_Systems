#First set: Safe Sequence: 1,2,3
#Second set: Not Safe State

#Function for checking if any given row is able to be completed.
def CheckRow(row,F):
    #boolean values for if the row is safe, and if the row is all 0's
    Safe = True
    all0 = True
    #if any number in the row is above 0, all0 becomes False
    for num in row:
        if num > 0:
            all0 = False
    #if all0 if False,
    if all0 == False:
        #Find out if row is safe. Return Safe boolean value
        for num in range(len(row)):
            if F[num] - row[num] < 0:
                Safe = False
        return Safe

#Function iterating the singular row function
def CheckAllRows(N,F):
    #Count is number of all 0 rows
    count = 0
    #Create Safe boolean, this time for whole function rather than just given row
    Safe = True
    #Check each individual row.
    #If it is all 0's, add 1 to count
    #If a row is safe, return the row number (from 0 to m-1)
    #If count == m, it is a safe state.
    for row in range(len(N)):
        if CheckRow(N[row],F) == None:
            count = count + 1
        elif CheckRow(N[row],F):
            return row
        if count == len(N):
            return Safe

#Function to create list with m nested lists
def CreateList(m):
    lis = []
    i = 0
    #Use while loop to append empty list with more empty lists.
    while i < m:
        lis.append([])
        i = i+1
    return lis

#Recursive function that updates F and prints final answer
def Bankers(N,F,ans):
    num = CheckAllRows(N,F)
    if type(num)==int:
        x = [num]
        ans= ans+x
    #Call check all rows function
    
    #If True is returned, it is a safe state
    if num == True:
        #Final safe row was not being added to list
        #This checks for what row num is missing and adds to end of list
        #Only runs if it is confirmed to be a safe state.
        for i in range(len(N)):
            if i not in ans:
                ans.append(i)
        for i in range(len(ans)):
            ans[i] = ans[i]+1
        result = ans
        print("It has a Safe Sequence, which is:",result)
    #If nothing is returned, it is not a safe state
    elif num == None:
        print("It is not a Safe State.")
    #If a row number is returned
    #Add that row to F, and set the row to 0
    #Call this Bankers function again with new N and F
    else:
        for integer in range(len(F)):
            F[integer] = N[num][integer] + F[integer]
            N[num][integer] = 0
        Bankers(N,F,ans)

#Initialize lists
m = int(input("Number of rows in C and A: "))
R = []
F = []
C = CreateList(m)
A = CreateList(m)
N = CreateList(m)

#Take input for list C
for num in range(1,m+1):
    print("------------------\nNow Entering row",num,"\n------------------")
    r = [int(inp) for inp in input("Enter the terms of the row of C, seperated by spaces: ").split()]
    C[num-1] = r

#Take input for list A
for num in range(1,m+1):
    print("Now Entering row",num,"\n------------------")
    r = [int(inp) for inp in input("Enter the terms of the row of A, seperated by spaces: ").split()]
    A[num-1] = r
print("------------------")
#Take input for list R
r = [int(inp) for inp in input("Enter the terms of R, seperated by spaces: ").split()]
R = r
print("------------------")
#Take input for list F
r = [int(inp) for inp in input("Enter the terms of F, seperated by spaces: ").split()]
F = r
print("------------------")
#Loops for calculating N given C and A
for row in range(len(C)):
    for num in range(len(C[0])):
        result = C[row][num] - A[row][num]
        N[row].append(result)

#Calling recursive Bankers function to return final result.
Bankers(N,F,[])
