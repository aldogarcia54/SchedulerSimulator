import sys
import random
import math

def FCFS():
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    while procsDone <= 10001:
        event = processes[procsDone]
        if event.arrivalTime < clock:
            waitTime = clock - event.arrivalTime
            readyQueueUsg += waitTime
        elif event.arrivalTime >= clock:
            nonUsage += event.arrivalTime - clock
            clock = event.arrivalTime
        event.completionTime = event.serviceTime + clock
        clock = event.completionTime
        turnaround += event.completionTime - event.arrivalTime
        procsDone += 1
    print(turnaround/procsDone)
    print(procsDone/clock)
    print(((clock-nonUsage)/clock)*100)
    print(readyQueueUsg/clock)

def SRTF():
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    while procsDone <= 10001:
        # find process in ready queue with shortest job time
        least = None
        process = None
        if len(readyQueue) == 0: # get next process in future
            process = processes[procsDone]
        else:
            id = 0
            least = readyQueue[0].remainingTime
            process = readyQueue[0]
            for i in range(len(readyQueue)):
                if readyQueue[i].remainingTime < least:
                    least = readyQueue[i].remainingTime
                    process = readyQueue[i]
                    id = i
            readyQueue.pop(id)
        # put process in cpu
        if process.arrivalTime < clock:
            waitTime = clock - process.arrivalTime
            readyQueueUsg += waitTime
        elif process.arrivalTime >= clock:
            nonUsage += process.arrivalTime - clock
            clock = process.arrivalTime

        process.completionTime = process.serviceTime + clock
        clock = process.completionTime
        procsDone += 1
        # put processes that arrived in the meantime in ready queue
        i = procsDone + len(readyQueue)
        while processes[i].arrivalTime <= clock:
            readyQueue.append(processes[i])
            i += 1
        turnaround += process.completionTime - process.arrivalTime
    print(turnaround / procsDone)
    print(procsDone / clock)
    print(((clock - nonUsage) / clock)*100)
    print(readyQueueUsg / clock)

def HRRN():
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    while procsDone <= 10001:
        # find process in ready queue with highest response ratio
        if len(readyQueue) == 0: # get next process in future
            process = processes[procsDone]
        else:
            id = 0
            highest = ((clock - readyQueue[0].arrivalTime) + readyQueue[0].serviceTime)/readyQueue[0].serviceTime
            process = readyQueue[0]
            for i in range(len(readyQueue)):
                RR = ((clock - readyQueue[i].arrivalTime) + readyQueue[i].serviceTime)/readyQueue[i].serviceTime
                if RR > highest:
                    highest = RR
                    process = readyQueue[i]
                    id = i
            readyQueue.pop(id)
        # put process in cpu
        if process.arrivalTime < clock:
            waitTime = clock - process.arrivalTime
            readyQueueUsg += waitTime
        elif process.arrivalTime >= clock:
            nonUsage += process.arrivalTime - clock
            clock = process.arrivalTime

        process.completionTime = process.serviceTime + clock
        clock = process.completionTime
        procsDone += 1
        # put processes that arrived in the meantime in ready queue
        i = procsDone + len(readyQueue)
        while processes[i].arrivalTime <= clock:
            readyQueue.append(processes[i])
            i += 1
        turnaround += process.completionTime - process.arrivalTime
    print(turnaround / procsDone)
    print(procsDone / clock)
    print(((clock - nonUsage) / clock)*100)
    print(readyQueueUsg / clock)

def RR():
    global procsDone
    global clock
    global processes
    global readyQueue
    global quantum
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    while procsDone <= 10001:
        # find process in ready queue to go next
        if len(readyQueue) == 0: # get next process in future
            process = processes[procsDone]
        else:
            process = readyQueue[0]
            readyQueue.pop(0)
        # put process in cpu
        if process.arrivalTime >= clock:
            nonUsage += process.arrivalTime - clock
            clock = process.arrivalTime
        # if process has enough time to finish, finish with process
        if process.remainingTime <= quantum:
            if process.arrivalTime < clock:
                waitTime = clock - process.arrivalTime
                readyQueueUsg += waitTime
            process.completionTime = process.remainingTime + clock
            clock = process.completionTime
            procsDone += 1
            turnaround += process.completionTime - process.arrivalTime
        # else put the process back in the ready queue
        else:
            process.remainingTime = process.remainingTime - quantum
            clock = quantum + clock
            readyQueue.append(process)
        # put processes that arrived in the meantime in ready queue
        i = procsDone + len(readyQueue)
        tempQueue = []
        while processes[i].arrivalTime <= clock:
            tempQueue.append(processes[i])
            i += 1
        readyQueue = tempQueue + readyQueue
    print(turnaround / procsDone)
    print(procsDone / clock)
    print(((clock - nonUsage) / clock)*100)
    print(readyQueueUsg / clock)

def generateProcesses():
    procs = []
    servRate = 1 / servTime
    time = 0
    for i in range(30000):
        randNum = random.random()
        while randNum == 0:
            randNum = random.random()
        randNum2 = random.random()
        while randNum2 == 0:
            randNum2 = random.random()
        randArrTime = -math.log(randNum)/arrRate
        time += randArrTime
        randServTime = -math.log(randNum2)/servRate
        proc = Process(i, randServTime, time, randServTime, 0)
        procs.append(proc)
    return procs

class Process:
    def __init__(self, id, serviceTime, arrivalTime, remainingTime, completionTime):
        self.id = id
        self.serviceTime = serviceTime
        self.arrivalTime = arrivalTime
        self.remainingTime = remainingTime
        self.completionTime = completionTime

# get input arguments
for i in range(len(sys.argv)):
    if sys.argv[i] == '-s' and i < (len(sys.argv) - 1):
        scheduler = int(sys.argv[i + 1])
    elif sys.argv[i] == '-a' and i < (len(sys.argv) - 1):
        arrRate = float(sys.argv[i + 1])
    elif sys.argv[i] == '-t' and i < (len(sys.argv) - 1):
        servTime = float(sys.argv[i + 1])
    elif sys.argv[i] == '-q' and i < (len(sys.argv) - 1):
        quantum = float(sys.argv[i + 1])

# Initialization
clock = 0
processes = generateProcesses()
procsDone = 0 # end condition (stop when 10,000 processes done)
readyQueue = []
cpuIdle = True

if scheduler == 1:
    FCFS()
elif scheduler == 2:
    SJF()
elif scheduler == 3:
    HRRN()
elif scheduler == 4:
    RR()