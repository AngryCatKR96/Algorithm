def NM(k): # 현재 배열에 k개를 입력했고 arr[k]를 정하는 함수
    # base condition
    if k == M:
        setted = set(arr)
        if setted not in checkedSet:
            checkedSet.append(setted)
            for i in arr:
                print(i, end=" ")
            print()
            return
        else:
            return
    
    # 중복체크를 조합에 대해서도 해야함
    for i in range(1,N+1):
        if checked[i] == False:
            arr[k] = i
            checked[i] = True
            NM(k+1)
            checked[i] = False
    
# 입력
N, M = map(int,input().split())

# 변수 정의
arr = [0 for _ in range(M)]
checked = [False for _ in range(N+1)]
checkedSet = list()

# 메서드실행
NM(0)