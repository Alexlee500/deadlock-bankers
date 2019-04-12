'''
Alexander Lee
989222904
Banker's Algorithm
Deadlock Detection

run with python3

'''
import sys

def readFile(fn):
    try:
        file = open(fn, "r")
    except:
        print ("Err: File not found")
        return -1
    return file

#evaluates available matrix and need matrix to determine if it can be run
def canRun(available, need):
    numTypes = len(available)
    #compare each element of the matrix. Return false if any available is less than need
    for i in range(0 + numTypes):
        if int(available[i]) < int(need[i]):
            return False
    return True

#adds the allocated resources to the available matrix
#returns a new value for available resources
def run(available, allocation):
    numTypes = len(available)
    newAvail = ''
    for i in range(0 + numTypes):
        newAvail += str(int(available[i]) + int(allocation[i]))
    return newAvail

def main():

    #checks arguments
    if (len(sys.argv) != 2):
        print ("Usage: python3 " + sys.argv[0] + " <filename>")
        return;

    #Takes first argument and reads as file
    fn = sys.argv[1]
    file = readFile(fn)

    #converts file to array
    arr = []
    for line in file:
        line = line.strip("\n")
        arr.append(line)

    #processes the array
    numProcesses = int(arr[0])
    numTypes = int(arr[1])
    available = arr[2]

    allocation= []
    for i in range(3, 3 + numProcesses):
        allocation.append(arr[i])

    need = []
    for i in range(3 + int(numProcesses), 3 + (2*numProcesses)):
        need.append(arr[i])

    max = []
    for i in range(0 + numProcesses):
        m = ''
        for j in range(0 + numTypes):
            m += str(int(allocation[i][j]) + int(need[i][j]))
        max.append(m)

    print ("Available:\t" , available)
    print ("Allocatiton:\t" , allocation)
    print ("Need:\t\t" , need)
    print ("Max:\t\t", max, "\n")

    counter = 0
    completed = []
    locked = []
    deadlocked = False
    while 1:
        processesRun = 0
        for i in range(0 + numProcesses):

            #if process is not yet completed, check if the process can run. Run the process
            if i not in completed:
                if canRun(available, need[i]):
                    #reset counter
                    counter = 0
                    #add to the processes run in current loop
                    processesRun += 1
                    #increase the available resources by the resources allocated to the process
                    available = run(available, allocation[i])
                    #add the process to the list of completed processes
                    completed.append(i)
            #if all the process are completed, exit the loop
        if len(completed) == numProcesses:
            deadlocked = False

            break

        #if there no processes were run during this loop, increment a counter by 1
        if processesRun == 0:
            #if no processes were run for a second loop,
            counter += 1
            if counter == 2:
                deadlocked = True

                # add all locked processes to an array
                for j in range(0 + numProcesses):
                    if j not in completed:
                        locked.append(j)
                break


    if deadlocked:
        print ("Deadlocked")
        print ("Locked processes")
        print (locked)

    else:
        print ("Not deadlocked")
        print ("Safe Execution Order:")
        print (completed)


main()
