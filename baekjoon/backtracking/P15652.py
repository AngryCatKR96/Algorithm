def NM(k): 
    if k == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    if k==0:
        for i in range(1,N+1):
            arr[k] = i
            NM(k+1)
    else:
        for i in range(arr[k-1],N+1):
            arr[k] = i
            NM(k+1)

N, M = map(int,input().split())

# 변수 정의
arr = [0 for _ in range(M)]

NM(0)