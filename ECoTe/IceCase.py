""" DFS와 아이스크림 개수 세기가 무슨 관계일까?
DFS==탐색, 아이스크림 개수 세기 == 0으로 어디까지 연결되어 있는지를 탐색
예제와 달리 연결은 다 되어있음
따라서 1이 방문처리의 역할을 함. 더 이상 탐색하지 못하게 하는 역할. 다른 범위으 0까지 가지 못하게 하는 역할

메서드정의(DFS) 재귀로 해주고 main에서 
(0,0)부터 탐색 시작 -> 연결된 모든 0을 탐색하고 방문처리함 -> 끝내면서 개수 +1
(0,1)은 (0,0) 탐색하면서 이미 방문처리 되어서 패스
..... 이렇게 진행하다보면 서로 떨어져있는 0을 방문처리 시작할때만 개수가 +1됨"""

def dfs(row, col, dataList):
    # index 범위 벗어났을 때 return
    if(row < 0 or N-1 < row): 
        return 
    if(col < 0 or M-1 < col):
        return 
     
    # 방문처리 되어있다면 return False
    if(dataList[row][col] == 1):
        return False
    # 방문처리 되어있지 않다면 True
    else:
        dataList[row][col] = 1 # 방문처리 해주고
        # 모든 방향에 대해서 재귀
        dfs(row+1, col, dataList) 
        dfs(row-1, col, dataList)
        dfs(row, col+1, dataList)
        dfs(row, col-1, dataList)
        return True
    

N, M = map(int, input().split())


iceCase = []
for i in range(N):
    iceCase.append(list(map(int, input())))
    
result = 0 # 아이스크림 개수    
for i in range(N):
    for j in range(M):
        if(dfs(i,j,iceCase)):
            result += 1
            
print(result)
        
    
