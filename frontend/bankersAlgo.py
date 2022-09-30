
def procMan(n,nR,a,c,cm,avail):

    global allocMatrix
    global maxMatrix
    global needMatrix
    global availMatrix

    allocMatrix = []
    maxMatrix = []
    needMatrix = []
    availMatrix = []

    nProcess = n
    nResources = nR
    allocMatrix = a
    if c=="max":
        maxMatrix = cm
        needMatrix = [[maxMatrix[i][j] - allocMatrix[i][j] for j in range(nResources)] for i in range(nProcess)]
    elif c=="need":
        needMatrix = cm
        maxMatrix = [[allocMatrix[i][j] + needMatrix[i][j] for j in range(nResources)] for i in range(nProcess)]
    
    availMatrix = avail



def banker():
    workStates = []
    safeSeq = []
    work = availMatrix.copy()
    workStates.append('Available -> '+' '.join(map(str,work)))
    finish = [False] * len(allocMatrix) 
    while any(all([needMatrix[i][j] <= work[j] for j in range(len(work))]) for i in range(len(finish)) if not finish[i]):
        for i in range(len(finish)):
            if not finish[i] and all([needMatrix[i][j] <= work[j] for j in range(len(work))]):
                work = [work[j] + allocMatrix[i][j] for j in range(len(work))]
                workStates.append('P'+str(i)+' -> '+' '.join(map(str,work)))
                finish[i] = True
                safeSeq.append('P' + str(i))
                # break
    if all(finish):
        print("Safe sequence: ", end = '')
        print(*safeSeq)
        print(workStates)
        return({'need':needMatrix,'safe':safeSeq,'work':workStates})
    else:
        print("Unsafe state")


# def resourceReq():
#     proc = int(input("Enter process number: "))
#     req = list(map(int, input("Enter request: ").split()))
#     if all([req[i] <= needMatrix[proc][i] for i in range(len(req))]):
#         if all([req[i] <= availMatrix[i] for i in range(len(req))]):
#             availMatrix = [availMatrix[i] - req[i] for i in range(len(req))]
#             allocMatrix[proc] = [allocMatrix[proc][i] + req[i] for i in range(len(req))]
#             needMatrix[proc] = [needMatrix[proc][i] - req[i] for i in range(len(req))]
#             banker()
#         else:
#             print("Request cannot be granted")
#     else:
#         print("Request cannot be granted")

def main():
    procMan()
    banker()

if __name__ == '__main__':
    main()