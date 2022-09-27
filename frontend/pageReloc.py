# Page relocation policies

def framMan(f,r):
    global n
    global ref
    n = f
    ref = r

def fifo():
    frameStates = []
    frames = []
    hm=[]
    faults = 0
    print('----------------------------------------------------------------------------')
    print('Page\t|\tH/M\t|\tMemory State')
    print('----------------------------------------------------------------------------')
    for i in range(len(ref)):
        print(ref[i],end='\t|\t')
        if len(frames)<n:
            frames.append(ref[i])
            frameStates.append(frames.copy())
            faults += 1
        else:
            if ref[i] in frames:
                print('Hit\t|')
                hm.append('H')
                frameStates.append(frames.copy())
                continue
            else:
                faults += 1
                frames.pop(0)
                frames.append(ref[i])
                frameStates.append(frames.copy())
        
        print('Miss\t|\t',frames)
        hm.append('M')

    print('\n\nNumber of page faults in FIFO policy : ',faults,'\n\n\n\n')
    print(frameStates)

    return({'pageFaults':faults,'pageFrames':frameStates,'hm':hm})

def LRU():
    frameStates = []
    frames = []
    faults = 0
    hm = []
    print('----------------------------------------------------------------------------')
    print('Page\t|\tH/M\t|\tMemory State')
    print('----------------------------------------------------------------------------')
    for i in range(len(ref)):
        print(ref[i],end='\t|\t')
        if len(frames)<n:
            frames.append(ref[i])
            frameStates.append(frames.copy())
            faults += 1
        else:
            if ref[i] in frames:
                print('Hit\t|')
                hm.append('H')
                frames.remove(ref[i])
                frames.append(ref[i])
                frameStates.append(frames.copy())
                continue
            else:
                frames.pop(0)
                frames.append(ref[i])
                frameStates.append(frames.copy())
                faults += 1
        
        print('Miss\t|\t',frames)
        hm.append('M')
    
    print('\n\nNumber of faults in LRU policy : ',faults,'\n\n\n\n')
    return({'pageFaults':faults,'pageFrames':frameStates,'hm':hm})

def optimal():
    frameStates = []
    frames = []
    faults = 0
    hm = []
    print('----------------------------------------------------------------------------')
    print('Page\t|\tH/M\t|\tMemory State')
    print('----------------------------------------------------------------------------')
    for i in range(len(ref)):
        print(ref[i],end='\t|\t')
        if len(frames)<n:
            frames.append(ref[i])
            frameStates.append(frames.copy())
            faults += 1
        else:
            if ref[i] in frames:
                print('Hit\t|')
                hm.append('H')
                frameStates.append(frames.copy())
                continue
            else:
                highestInd = 0
                highestIndFrame = 0

                for frameInd in range(len(frames)):
                    curFrame = frames[frameInd]
                    if curFrame not in ref[i:]:
                        frames.remove(curFrame)
                        frames.append(ref[i])
                        frameStates.append(frames.copy())
                        faults += 1
                        yes = False
                        break
                    else:
                        yes = True                
                        curInd = ref[i:].index(curFrame)
                        if curInd > highestInd:
                            highestInd = curInd
                            highestIndFrame = frameInd

                if yes:
                    frames.pop(highestIndFrame)
                    frames.append(ref[i])
                    frameStates.append(frames.copy())
                    faults += 1
        print('Miss\t|\t',frames)
        hm.append('M')
    print('\n\nNumber of faults in optimal policy : ',faults,'\n\n\n\n')
    return({'pageFaults':faults,'pageFrames':frameStates,'hm':hm})
