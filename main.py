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

def generateProcesses():
    procs = []
    servRate = 1 / servTime
    time = 0
    for i in range(10020):
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

'''while procsDone <= 10001:
    event = getEvent()
    clock = event.time
    if event.type == "ARR":
        processArrival(event)
    else:
        processDeparture(event)'''
