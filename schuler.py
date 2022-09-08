
class Process:
    
    def __init__(self,n,a,s):
        self.name = n
        self.arrivalTime = a
        self.serviceTime = s

        self.leftT = s
        self.finishT=0
        self.priority=1
    
    def execute(self,n):
        if n:
            if n < self.leftT:
                self.leftT-=n
            else:
                retVal = n - self.leftT
                self.leftT=0
                return retVal
        else:
            self.leftT-=1

    def reset(self):
        self.leftT = self.serviceTime
        self.finishT = 0
        self.priority=1

    def tally(self):
        self.TAT = self.finishT - self.arrivalTime
        self.WT = self.TAT - self.serviceTime

class GanttSection:
    def __init__(self,s,e,p):
        self.sT = s
        self.endT = e
        self.process = p

def displayGanttChart(ganttChart):
    print('Gantt Chart: ')
    for section in ganttChart:
        if not section.process == 'Idle':
            print(section.sT,'-',section.endT,':',section.process.name)
        else:
            print(section.sT,'-',section.endT,':',section.process)

def scheduler():
    global pool
    pool = []
    global trt 
    trt = 0
    n = int(input("Number of processes: "))
    for i in range(n):
        a = int(input('Enter arrival time: '))
        b = int(input('Enter burst time: '))
        trt += b
        x = Process('P'+str(i+1),a,b)
        pool.append(x)
    
    # sort pool on basis of arrival time
    pool.sort(key=lambda x: x.arrivalTime)

def fcfs():

    elapsedTime = 0

    ttat=0
    twt=0

    arrivalIndex = 0
    readyQ = []

    curProcess = 0

    ganttChart = []

    while elapsedTime<trt:
        for process in pool[arrivalIndex:]:
            if process.arrivalTime <= elapsedTime:
                readyQ.append(process)
                arrivalIndex+=1
            else:
                break

        if readyQ:
            curProcess = readyQ.pop(0)
            g = GanttSection(elapsedTime,elapsedTime+curProcess.leftT,curProcess)
            ganttChart.append(g)
            elapsedTime += curProcess.leftT
            curProcess.execute(curProcess.leftT)
            curProcess.finishT = elapsedTime
            curProcess.tally()

            ttat += curProcess.TAT
            twt += curProcess.WT
        else:
            g = GanttSection(elapsedTime,elapsedTime+1,'Idle')
            elapsedTime+=1

    displayGanttChart(ganttChart)

    print('Process\tArrival Time\tBurst Time\tFinish Time\tTurnaround Time\tWaiting Time')
    for process in pool:
        print(process.name,'\t',process.arrivalTime,'\t\t',process.serviceTime,'\t\t',process.finishT,'\t\t',process.TAT,'\t\t\t',process.WT)
    
    print('Total turnaround time: ',ttat)
    print('Average turnaround time: ',ttat/len(pool))
    print('Total waiting time: ',twt)
    print('Average waiting time: ',twt/len(pool))

def sjf(preemption):
    elapsedTime = 0

    ttat=0
    twt=0

    arrivalIndex = 0
    readyQ = []

    curProcess = 0

    ganttChart = []

    while elapsedTime<trt:            
        # prepare readyQ for processes that are ready to be executed
        
        for process in pool[arrivalIndex:]:
            if process.arrivalTime <= elapsedTime:
                readyQ.append(process)
                arrivalIndex+=1
            else:
                break
        
        if readyQ:
            readyQ.sort(key=lambda x: x.leftT)
            curProcess = readyQ.pop(0)

        if curProcess and not preemption:
            g = GanttSection(elapsedTime,elapsedTime+curProcess.leftT,curProcess)
            ganttChart.append(g)
            elapsedTime += curProcess.leftT
            curProcess.execute(curProcess.leftT)
            curProcess.finishT = elapsedTime
            curProcess.tally()

            ttat += curProcess.TAT
            twt += curProcess.WT
        elif curProcess and preemption:
            g= GanttSection(elapsedTime,elapsedTime+1,curProcess)
            ganttChart.append(g)
            elapsedTime += 1
            curProcess.execute(1)
            if curProcess.leftT == 0:
                curProcess.finishT = elapsedTime
                curProcess.tally()
                ttat += curProcess.TAT
                twt += curProcess.WT
                curProcess = 0
            else:
                readyQ.append(curProcess)
                curProcess = 0
        else:
            g = GanttSection(elapsedTime,elapsedTime+1,'Idle')
            elapsedTime+=1

    # merge gantt sections if preemtion is enabled
    if preemption:
        i=0
        while i<len(ganttChart)-1:
            if ganttChart[i].process == ganttChart[i+1].process:
                ganttChart[i].endT = ganttChart[i+1].endT
                ganttChart.pop(i+1)
            else:
                i+=1

    displayGanttChart(ganttChart)
    
    print('Process\tArrival Time\tBurst Time\tFinish Time\tTurnaround Time\tWaiting Time')
    for process in pool:
        print(process.name,'\t',process.arrivalTime,'\t\t',process.serviceTime,'\t\t',process.finishT,'\t\t',process.TAT,'\t\t\t',process.WT)
    
    print('Total turnaround time: ',ttat)
    print('Average turnaround time: ',ttat/len(pool))
    print('Total waiting time: ',twt)
    print('Average waiting time: ',twt/len(pool))

def priority(preemption):
    elapsedTime = 0

    ttat=0
    twt=0

    arrivalIndex = 0
    readyQ = []

    curProcess = 0

    ganttChart = []

    #set priority
    for process in pool:
        process.priority = int(input('Enter priority for '+process.name+': '))


    while elapsedTime<trt:            
        # prepare readyQ for processes that are ready to be executed
        for process in pool[arrivalIndex:]:
            if process.arrivalTime <= elapsedTime:
                readyQ.append(process)
                arrivalIndex+=1
            else:
                break
        
        if readyQ:
            readyQ.sort(key=lambda x: x.priority)
            curProcess = readyQ.pop(0)

        if curProcess and not preemption:
            g = GanttSection(elapsedTime,elapsedTime+curProcess.leftT,curProcess)
            ganttChart.append(g)
            elapsedTime += curProcess.leftT
            curProcess.execute(curProcess.leftT)
            curProcess.finishT = elapsedTime
            curProcess.tally()

            ttat += curProcess.TAT
            twt += curProcess.WT
        elif curProcess and preemption:
            g= GanttSection(elapsedTime,elapsedTime+1,curProcess)
            ganttChart.append(g)
            elapsedTime += 1
            curProcess.execute(1)
            if curProcess.leftT == 0:
                curProcess.finishT = elapsedTime
                curProcess.tally()
                ttat += curProcess.TAT
                twt += curProcess.WT
                curProcess = 0
            else:
                readyQ.append(curProcess)
                curProcess = 0
        else:
            g = GanttSection(elapsedTime,elapsedTime+1,'Idle')
            elapsedTime+=1

    # merge gantt sections if preemtion is enabled
    if preemption:
        i=0
        while i<len(ganttChart)-1:
            if ganttChart[i].process == ganttChart[i+1].process:
                ganttChart[i].endT = ganttChart[i+1].endT
                ganttChart.pop(i+1)
            else:
                i+=1

    displayGanttChart(ganttChart)
    
    print('Process\tArrival Time\tBurst Time\tFinish Time\tTurnaround Time\tWaiting Time')
    for process in pool:
        print(process.name,'\t',process.arrivalTime,'\t\t',process.serviceTime,'\t\t',process.finishT,'\t\t',process.TAT,'\t\t\t',process.WT)
    
    print('Total turnaround time: ',ttat)
    print('Average turnaround time: ',ttat/len(pool))
    print('Total waiting time: ',twt)
    print('Average waiting time: ',twt/len(pool))

def rr(q):
    elapedTime = 0

    ttat=0
    twt=0

    arrivalIndex = 0
    readyQ = []

    curProcess = 0

    ganttChart = []
    insertion = False

    while elapedTime<trt:
        # prepare readyQ for processes that are ready to be executed
        for process in pool[arrivalIndex:]:
            if process.arrivalTime <= elapedTime:
                if insertion:
                    readyQ.insert(-1,process)
                else:
                    readyQ.append(process)
                arrivalIndex+=1
            else:
                break
            

        if readyQ:

            curProcess = readyQ.pop(0)
            
            g = GanttSection(elapedTime,'N/A',curProcess)
            
            
            exec = curProcess.execute(q)

            if exec:
                elapedTime += q-exec
            else:
                elapedTime += q

            g.endT = elapedTime
            ganttChart.append(g)

            if curProcess.leftT == 0:
                curProcess.finishT = elapedTime
                curProcess.tally()
                ttat += curProcess.TAT
                twt += curProcess.WT
                insertion = False
            else:
                insertion = True
                readyQ.append(curProcess)
        
        else:
            g = GanttSection(elapedTime,elapedTime+1,'Idle')
            elapedTime+=1

    #merge gantt sections
    i=0
    while i<len(ganttChart)-1:
        if ganttChart[i].process == ganttChart[i+1].process:
            ganttChart[i].endT = ganttChart[i+1].endT
            ganttChart.pop(i+1)
        else:
            i+=1

    displayGanttChart(ganttChart)

    print('Process\tArrival Time\tBurst Time\tFinish Time\tTurnaround Time\tWaiting Time')
    for process in pool:
        print(process.name,'\t',process.arrivalTime,'\t\t',process.serviceTime,'\t\t',process.finishT,'\t\t',process.TAT,'\t\t\t',process.WT)

    print('Total turnaround time: ',ttat)
    print('Average turnaround time: ',ttat/len(pool))
    print('Total waiting time: ',twt)
    print('Average waiting time: ',twt/len(pool))

def resetAll():
    for process in pool:
        process.reset()

if __name__ == '__main__':
    scheduler()

    print('FCFS')
    fcfs()
    
    resetAll()
    print('SJF')
    sjf(False)
    
    resetAll()
    print('SJF with preemption')
    sjf(True)
    
    resetAll()
    print('Priority')
    priority(False)
    
    resetAll()
    print('Priority with preemption')
    priority(True)
    
    resetAll()
    print('Round Robin')
    q = int(input('Enter quantum: '))
    rr(q)
