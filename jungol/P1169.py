import sys
# 재귀 -> 뭐를 +1 해줘야할까? index값! base condition이 오히려 작아지는게 아닌 index의 끝을보는게 됨
def dice(depth, arr):
    global savedList
    
    if(M == 1):
        for i in range(1,7):
            arr[depth] = i
            if(depth < N-1): # recursion
                dice(depth+1, arr)
            else: # base condition
                printArr(arr)
    # 중복 제거 >> [1,1,2] [1,2,1] [2,1,1]이 같다? 어떻게 같게 만들어줄 수 있을까. > 정렬 후 비교? > 시간복잡도가 좀.. > 정올은 테케가 적으니 할만할지도 
    # 근데 비교하려면 배열 저장해야하는데?
    elif(M == 2):
        for i in range(1,7):
            arr[depth] = i
            if(depth < N-1): # recursion
                dice(depth+1, arr)
            else: # base condition
                sortedList = sorted(arr)
                if sortedList not in savedList:
                    savedList.append(sortedList)
                    printArr(arr) 
    # 모든 다른 수 >> 한 배열안에서 같은 수가 있으면 안됨
    else:
        for i in range(1,7):
            if(i not in arr[:depth]):
                arr[depth] = i
            else:
                continue
            
            if(depth < N-1): # recursion
                dice(depth+1, arr)
            else: # base condition
                printArr(arr)
        
        
def printArr(arr):
    for i in arr:
        print(i, end=" ")
    print()

N, M = map(int,sys.stdin.readline().strip().split())

depth = 0
arr = [0]*N
savedList = []

dice(depth, arr)