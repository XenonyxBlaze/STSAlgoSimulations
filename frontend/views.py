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
        # try:

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

        # except Exception as e:
        #     print('Invalid form\n',e)
        #     return render(request,'sts.html',context={'invalid':True,'msg':e})
    else:
        return redirect('sts')