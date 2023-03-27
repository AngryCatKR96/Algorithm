import sys

t = int(sys.stdin.readline().strip())

resultList = [[] for _ in range(t)]
for i in range(t):
    
    n, s, r = map(int, sys.stdin.readline().strip().split())
    
    max = s - r
    
    # max 결과 리스트에 추가
    resultList[i].append(max)
    
    # 결과리스트의 길이가 n개가 맞고 
    while s-max > max:
        resultList[i].append(max)
        s -= max
    resultList[i].append(s-max)
        
    if len(resultList[i]) != n:
        for j in range(1, len(resultList[i])):
            while resultList[i][j] > 1 and len(resultList[i])<n:
                resultList[i][j] -= 1
                resultList[i].append(1)
            if len(resultList[i]) == n:
                break
            
#출력
for i in range(t):
    for j in resultList[i]:
        print(j, end=" ")
    print()
        