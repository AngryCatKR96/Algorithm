import sys

t = int(sys.stdin.readline().strip())

# 전체 매트릭스 생성
finalList = [[] for _ in range(t)]
for k in range(t):
    n = int(sys.stdin.readline().strip())
    
    # 입력을 기반으로 행렬 생성
    matrix = [[0 for _ in range(n-1)] for _ in range(n)]
    for j in range(n):
            matrix[j] = list(map(int,sys.stdin.readline().strip().split()))
            
    # 대각을 기준으로 대칭 행렬 생성
    tr_matrix = [[0 for _ in range(n)] for _ in range(n-1)]
    for i in range(n):
        for j in range(n-1):
            tr_matrix[j][i] = matrix[i][j]
    
    # 대칭행렬의 규칙성을 통해 원래 수열을 찾는 과정    
    resultList = [0]*n   
    temp = 0
    for i in range(n):
        # 첫번째 행에서 가장 많은 수가 수열의 첫번째 값이고 나머지 값이 두번째 값임
        if i==0:
            count1 = tr_matrix[i].count(max(tr_matrix[i]))
            count2 = tr_matrix[i].count(min(tr_matrix[i]))
            if count1 > count2:
                resultList[i] = max(tr_matrix[i])
                temp = min(tr_matrix[i])
            else:
                resultList[i] = min(tr_matrix[i])
                temp = max(tr_matrix[i])
        # 두번째 행부턴 앞의 행에서 남은 값들이 먼저 오고 나머지 값들이 다음에 옴
        else:
            resultList[i] = temp
            # 가장 마지막 행에서는 남는 값이 존재하지 않으므로 인덱스 에러를 방지해준다.
            if i==n-1: 
                continue
            else:
                temp = list(set(tr_matrix[i])-set([temp]))[0]
    
    finalList[k] = resultList

for i in range(t):
    for j in finalList[i]:
        print(j, end=" ")
    print()

    
