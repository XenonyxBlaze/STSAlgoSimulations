from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, 'index.html')

def sts(request):
    return render(request, 'sts.html',context={'invalid':False})

def bankers(request):
    return render(request, 'banker.html')

def pagereloc(request):
    return render(request, 'pagereloc.html')

def disksched(request):
    return render(request, 'diskScheduler.html')

from . import stsAlgos

def stsoutput(request):
    if request.method=="POST":
        try:

            algo = request.POST.get('algo')
            print(algo)
            n = int(request.POST.get('numProc'))
            print(n)
            arrT = list(map(int, request.POST.get('arrT').split()))
            if len(arrT) != n:
                raise Exception('Bad Input for arrival time')
            print(arrT)

            burstT = list(map(int, request.POST.get('burstT').split()))
            if len(burstT) != n:
                raise Exception('Bad Input for burst time')
            print(burstT)

            
            if algo == "sjf" or algo == "prio":
                preempt = bool(int(request.POST.get('preempt')))
                print(preempt)
            if algo == "prio":
                prio = list(map(int, request.POST.get('prior').split()))
                if len(prio) != n:
                    raise Exception('Bad Input for priority')
                print(prio)
            if algo == "robin":
                quantum = int(request.POST.get('quantum'))
                if quantum <= 0:
                    raise Exception('Bad Input for quantum')
                print(quantum)

            if algo == 'fcfs':
                stsAlgos.scheduler(n, arrT, burstT, algo, None)
                stsReturn = stsAlgos.fcfs()
            elif algo == 'sjf':
                stsAlgos.scheduler(n, arrT, burstT, algo, None)
                stsReturn = stsAlgos.sjf(preempt)
            elif algo == 'prio':
                stsAlgos.scheduler(n, arrT, burstT, algo, prio)
                stsReturn = stsAlgos.priority(preempt)
            elif algo == 'robin':
                stsAlgos.scheduler(n, arrT, burstT, algo, None)
                stsReturn = stsAlgos.rr(quantum)
            else:
                raise Exception('Bad Input for algo')
            
            
            return render(request, 'stsoutput.html',context={'invalid':False,'algo':algo,'gantt':stsReturn['gantt'],'pool':stsReturn['pool'],'ttat':stsReturn['ttat'],'twt':stsReturn['twt'],'atat':stsReturn['atat'],'awt':stsReturn['awt']})

        except Exception as e:
            print('Invalid form\n',e)
            return render(request,'sts.html',context={'invalid':True,'msg':e})
    else:
        return redirect('sts')

from . import bankersAlgo

def bankersoutput(request):
    if request.method=="POST":
        try:
            n = int(request.POST.get('numProc'))
            print(n)
            nR = int(request.POST.get('numRes'))
            print(nR)
            alloc = list(request.POST.get('allocMat').split('\r\n'))
            if len(alloc) != n:
                raise Exception('Bad Input for allocation')
            print(alloc)
            for i in range(n):
                alloc[i] = list(map(int, alloc[i].split()))
                if len(alloc[i]) != nR:
                    raise Exception('Bad Input for allocation')
            print(alloc)

            c = request.POST.get('man')

            cm = list(request.POST.get('calcMat').split('\r\n'))
            if len(cm) != n:
                raise Exception('Bad Input for max')
            print(cm)
            for i in range(n):
                cm[i] = list(map(int, cm[i].split()))
                if len(cm[i]) != nR:
                    raise Exception('Bad Input for max')
            print(cm)

            avail = list(map(int,request.POST.get('avail').split()))
            if len(avail) != nR:
                raise Exception('Bad Input for available')
            print(avail)

            bankersAlgo.procMan(n, nR, alloc, c, cm, avail)
            bankersReturn = bankersAlgo.banker()
            return render(request, 'bankerout.html',context={'invalid':False,'n':range(n),'nR':range(nR),'alloc':alloc,'need':bankersReturn['need'],'safe':bankersReturn['safe'],'work':bankersReturn['work']})

        except Exception as e:
            print('Invalid form\n',e)
            return render(request,'banker.html',context={'invalid':True,'msg':e})
    else:
        return redirect('bankers')

from . import pageReloc

def pagerelocoutput(request):
    if request.method=="POST":
        try:
            n = int(request.POST.get('numFrames'))
            print(n)
            ref = list(map(int,request.POST.get('refStr').split()))
            print(ref)
            algo = request.POST.get('algo')
            print(algo)
            if algo == 'fifo':
                pageReloc.framMan(n, ref)
                pageRelocReturn = pageReloc.fifo()
            elif algo == 'lru':
                pageReloc.framMan(n, ref)
                pageRelocReturn = pageReloc.LRU()
            elif algo == 'optimal':
                pageReloc.framMan(n, ref)
                pageRelocReturn = pageReloc.optimal()
            else:
                raise Exception('Bad Input for algo')
            return render(request, 'pagerelocout.html',context={'invalid':False,'algo':algo,'ref':ref,'frames':n,'nf':range(n),'n':range(len(ref)),'pageFaults':pageRelocReturn['pageFaults'],'hmL':pageRelocReturn['hm'],'pageFrames':pageRelocReturn['pageFrames']})

        except Exception as e:
            print('Invalid form\n',e)
            return render(request,'pagereloc.html',context={'invalid':True,'msg':e})
    else:
        return redirect('pagereloc')