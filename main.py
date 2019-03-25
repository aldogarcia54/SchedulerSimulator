import sys
import random
import math

def FCFS():
    # TODO: maybe take a look into implementing readyqueue to find ready queue usage
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    readyQueue.append(processes[procsDone])
    while procsDone <= 10001:
        event = processes[procsDone]
        if event.arrivalTime < clock:
            waitTime = clock - event.arrivalTime
            readyQueueUsg += waitTime
        elif event.arrivalTime > clock:
            nonUsage += event.arrivalTime - clock
            clock = event.arrivalTime
        event.completionTime = event.serviceTime + clock
        clock = event.completionTime
        # put processes in ready queue
        t = True
        i = procsDone + 1
        if len(readyQueue) > 0:
            readyQueue = readyQueue[1:]
        while t:
            if processes[i].arrivalTime < clock:
                readyQueue.append(processes[i])
                i += 1
            else:
                t = False
        processes[procsDone] = event
        turnaround += event.completionTime - event.arrivalTime
        procsDone += 1
    print("Turnaround: ",turnaround/procsDone,"seconds")
    print("Throughput: ",procsDone/clock,"procs/sec")
    print("CPU Utilization: ",(clock-nonUsage)/clock,"%")
    print("Avg number of processes in ready queue: ",readyQueueUsg/clock,"processes")

def SJF():
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    i = 0
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
        # put processes that arrived in the meantime in ready queue
        while processes[i].arrivalTime <= clock:
            readyQueue.append(process)
            i += 1
        readyQueueUsg += len(readyQueue)
        turnaround += process.completionTime - process.arrivalTime
        procsDone += 1
    print("Turnaround: ", turnaround/procsDone, "seconds")
    print("Throughput: ", procsDone/clock ,"procs/sec")
    print("CPU Utilization: ", (clock-nonUsage)/clock, "%")
    print("Avg number of processes in ready queue: ", readyQueueUsg/procsDone, "processes")

def HRRN():
    global procsDone
    global clock
    global processes
    global readyQueue
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    i = 0
    while procsDone <= 10001:
        # find process in ready queue with highest response ratio
        least = None
        process = None
        if len(readyQueue) == 0: # get next process in future
            process = processes[procsDone]
        else:
            id = 0
            highest = ((clock - readyQueue[0].arrivalTime) + readyQueue[0].serviceTime)/readyQueue[0].serviceTime
            process = readyQueue[0]
            for i in range(len(readyQueue)):
                RR = ((clock - readyQueue[i].arrivalTime) + readyQueue[i].serviceTime)/readyQueue[i].serviceTime
                if RR > highest:
                    highest = readyQueue[i].remainingTime
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
        # put processes that arrived in the meantime in ready queue
        while processes[i].arrivalTime <= clock:
            readyQueue.append(process)
            i += 1
        readyQueueUsg += len(readyQueue)
        turnaround += process.completionTime - process.arrivalTime
        procsDone += 1
    print("Turnaround: ", turnaround/procsDone, "seconds")
    print("Throughput: ", procsDone/clock ,"procs/sec")
    print("CPU Utilization: ", (clock-nonUsage)/clock, "%")
    print("Avg number of processes in ready queue: ", readyQueueUsg/procsDone, "processes")

def RR():
    global procsDone
    global clock
    global processes
    global readyQueue
    global quantum
    turnaround = 0
    nonUsage = 0
    readyQueueUsg = 0
    i = 0
    while procsDone <= 10001:
        # find process in ready queue with highest response ratio
        least = None
        process = None
        if len(readyQueue) == 0:  # get next process in future
            process = processes[procsDone]
        else:
            id = 0
            highest = ((clock - readyQueue[0].arrivalTime) + readyQueue[0].serviceTime) / readyQueue[0].serviceTime
            process = readyQueue[0]
            for i in range(len(readyQueue)):
                RR = ((clock - readyQueue[i].arrivalTime) + readyQueue[i].serviceTime) / readyQueue[i].serviceTime
                if RR > highest:
                    highest = readyQueue[i].remainingTime
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
        # put processes that arrived in the meantime in ready queue
        while processes[i].arrivalTime <= clock:
            readyQueue.append(process)
            i += 1
        readyQueueUsg += len(readyQueue)
        turnaround += process.completionTime - process.arrivalTime
        procsDone += 1
    print("Turnaround: ", turnaround / procsDone, "seconds")
    print("Throughput: ", procsDone / clock, "procs/sec")
    print("CPU Utilization: ", (clock - nonUsage) / clock, "%")
    print("Avg number of processes in ready queue: ", readyQueueUsg / procsDone, "processes")

def generateProcesses():
    procs = []
    servRate = 1 / servTime
    time = 0
    for i in range(20000):
        randNum = random.random()
        while randNum == 0:
            randNum = random.random()
        randNum2 = random.random()
        while randNum2 == 0:
            randNum2 = random.random()
        randArrTime = -math.log(randNum)/arrRate
        time += randArrTime
        randServTime = -math.log(randNum2)/servRate
        proc = Process(i, randServTime, time, randServTime, 0) # TODO: fix completion time variable
        procs.append(proc)
    return procs


#def scheduleEvent(type, time):
    # creates new event and places it in the event queue
    # TODO


def processArrival(event):
    global cpuIdle
    if cpuIdle:
        cpuIdle = False
        scheduleEvent("DEP", event.time + serviceTime)
    #else:
        # TODO: put event in readyQueue
    # TODO: scheduleEvent("ARR",...) : schedule next arrival?????

def processDeparture(event):
    global cpuIdle
    if readyQueue == []:
        cpuIdle = True
    else:
        # TODO: remove process from ready queue
        scheduleEvent("DEP", event.time + serviceTime)

class Process:
    def __init__(self, id, serviceTime, arrivalTime, remainingTime, completionTime):
        self.id = id
        self.serviceTime = serviceTime
        self.arrivalTime = arrivalTime
        self.remainingTime = remainingTime
        self.completionTime = completionTime

class eventNode:
    def __init__(self, time, action, process):
        self.time = time
        self.action = action
        self.process = process
        self.next = None

    def addNext(self, node):
        if self.next == None:
            self.next = node
        else:
            self.next.addNext(node)

class eventQueue:
    def __init__(self):
        self.head = None

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
'''for process in processes:
    print(process.completionTime)'''
procsDone = 0 # end condition (stop when 10,000 processes done)
readyQueue = []
cpuIdle = True
eventQueue = eventQueue()

if scheduler == 1:
    FCFS()
    #for proc in processes:
        #print(proc.completionTime)
elif scheduler == 2:
    SJF()
elif scheduler == 3:
    HRRN()
elif scheduler == 4:
    RR()

'''while procsDone <= 10001:
    event = getEvent()
    clock = event.time
    if event.type == "ARR":
        processArrival(event)
    else:
        processDeparture(event)'''
