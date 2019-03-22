import sys
import random
import math

def scheduleEvent(type, time)
def processArrival(event)
def processDeparture(event)
def generateProcesses()


# get input arguments
for i in range(len(sys.argv)):
    if sys.argv[i] == '-s' and i < (len(sys.argv) - 1):
        scheduler = sys.argv[i + 1]
    elif sys.argv[i] == '-a' and i < (len(sys.argv) - 1):
        arrRate = sys.argv[i + 1]
    elif sys.argv[i] == '-t' and i < (len(sys.argv) - 1):
        servTime = sys.argv[i + 1]
    elif sys.argv[i] == '-q' and i < (len(sys.argv) - 1):
        quantum = sys.argv[i + 1]

# Initialization
clock = 0
processes = generateProcesses()
print(processes)
procsDone = 0 # end condition (stop when 10,000 processes done)
readyQueue = []
cpuIdle = True
#eventQueue = eventQueue()

#
while procsDone <= 10001:
    event = getEvent()
    clock = event.time
    if event.type == "ARR":
        processArrival(event)
    else:
        processDeparture(event)

def generateProcesses():
    processes = []
    servRate = 1 / servTime
    time = 0
    for i in range(10020):
        randNum = random.random()
        while randNum == 0:
            randNum = random.random()
        randNum2 = random.random()
        while randNum2 == 0:
            randNum2 = random.random()
        randArrTime = math.log(randNum)/arrRate
        time += randArrTime
        randServTime = math.log(randNum2)/servRate
        # TODO: create process and add it to list
        processes.append(randArrTime)
    return processes


def scheduleEvent(type, time):
    # creates new event and places it in the event queue
    # TODO

def processArrival(event):
    global cpuIdle
    if cpuIdle:
        cpuIdle = False
        scheduleEvent("DEP", event.time + serviceTime)
    else:
        # TODO: put event in readyQueue
    # TODO: scheduleEvent("ARR",...) : schedule next arrival?????

def processDeparture(event):
    global cpuIdle
    if readyQueue == []:
        cpuIdle = True
    else:
        # remove process from ready queue
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