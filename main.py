import sys

def main():
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

def scheduleEvent(type, time, ...):
    # creates new event and places it in the event queue

class Process:
    def __init__(self, id, serviceTime, arrivalTime, remainingTime, completionTime):
        self.id = id
        self.serviceTime = serviceTime
        self.arrivalTime = arrivalTime
        self.remainingTime = remainingTime
        self.completionTime = completionTime

main()