def NM(k): # 현재 배열에 k개의 원소가 들어가 있고 arr[k]를 정하는 함수
    # baes condition k == M이면 배열 출력하고 리턴
    if k == M:
        for i in arr:
            print(i, end=" ")
        print()
        return
    # k!=M이면 그 숫자가 사용되었는지 체크 후 False면 True로 바꾸고 배열에 넣음
    for i in range(1,N+1):
        if checked[i] == False:
            arr[k] = i
            checked[i] = True 
            NM(k+1)
            checked[i] = False # 다 사용했다면 False처리 해줘야 다른 경로에서 또 사용할 수 있음

N, M = map(int,input().split())

# 변수 정의
arr = [0 for _ in range(M)]
checked = [False for _ in range(N+1)]

NM(0)
