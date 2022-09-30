
def FCFS(dr,h):
    seq = []
    diskReqs = dr
    head = h
    print('----------------------------------------------------------------------------')
    print('Request\t|\tHead Movement')
    print('----------------------------------------------------------------------------')
    total = 0
    for i in range(len(diskReqs)):
        print(diskReqs[i],end='\t|\t')
        seq.append(diskReqs[i])
        if diskReqs[i] == head:
            continue
        else:
            print(abs(diskReqs[i]-head))
            total += abs(diskReqs[i]-head)
            head = diskReqs[i]
    
    print('\n\nTotal head movement in FCFS policy : ',total,'\n\n\n\n')

    return({'seq':seq,'seek':total})

def SSTF(dr,h):
    seq=[]
    diskReqs = dr.copy()
    head = h
    print('----------------------------------------------------------------------------')
    print('Request\t|\tHead Movement')
    print('----------------------------------------------------------------------------')
    total = 0
    diskReqs.sort()
    while len(diskReqs) > 0:
        j=0
        while True:
            if diskReqs[j]<head:
                j+=1
                continue
            else:
                def1 = abs(diskReqs[j]-head)
                def2 = abs(diskReqs[j-1]-head)
                if def1<def2:
                    print(diskReqs[j],end='\t|\t')
                    seq.append(diskReqs[j])
                    print(def1)
                    total += def1
                    head = diskReqs[j]
                    diskReqs.pop(j)
                    break
                else:
                    print(diskReqs[j-1],end='\t|\t')
                    seq.append(diskReqs[j-1])
                    print(def2)
                    total += def2
                    head = diskReqs[j-1]
                    diskReqs.pop(j-1)
                    break

    print('\n\nTotal head movement in SSTF policy : ',total,'\n\n\n\n')

    return({'seek':total,'seq':seq})

def binSearch(arr,x):
    
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<x and arr[mid+1]>x:
            return mid+1
        elif arr[mid]>x and arr[mid+1]<x:
            return mid
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return low

def SCAN(dr,h,c):
    seq=[]
    head = h
    diskReqs = dr.copy()
    total = 0
    diskReqs.sort()
    split = binSearch(diskReqs,head)

    f = diskReqs[split:]
    b = diskReqs[:split]
    if not c:
        b.reverse()
    else:
        f.append(199)
        b.insert(0,0)

    diskReqs = f+b    

    print('----------------------------------------------------------------------------')
    print('Request\t|\tHead Movement')
    print('----------------------------------------------------------------------------')
    
    for i in range(len(diskReqs)):
        print(diskReqs[i],end='\t|\t')
        seq.append(diskReqs[i])
        if diskReqs[i] == head:
            continue
        else:
            print(abs(diskReqs[i]-head))
            total += abs(diskReqs[i]-head)
            head = diskReqs[i]
    
    x = lambda c: 'C-' if c else ''
    print('\n\nTotal head movement in',x(c),'SCAN policy : ',total,'\n\n\n\n')

    return({'seq':seq,'seek':total})
