"""최소 이동칸의 개수를 구해야함. DFS, BFS 문제이므로 탐색 문제임 어떻게 카운트를 해줘야할까?
얼음틀 문제와 마찬가지로 상하좌우로 재귀적으로 탐색하는데 범위를 벗어나거나 해당 위치가 0일 경우엔 끝
위치가 N-1,M-1이라면 카운트 출력, 현재 카운트도 다음 재귀 메서드로 넘겨줘야하니 카운트도 매개변수에 있어야하지 않을까?
그럼 row, col, dataList, count 네 개의 매개변수를 갖겠지?"""
N, M = map(int, input().split())

# 미로 생성
maze = []
for i in range(N):
    maze.append(list(map(int, input())))
    
    
# dfs 매서드
def dfs(row, col, dataList, cnt):
    # index 범위 벗어나면 return
    if(row < 0 or N-1 < row or col < 0 or M-1 < col) : 
        return 
    
    # 해당 위치의 값이 0이면 return
    if(dataList[row][col] == 0):
        return
    # 해당 위치의 값이 1이면 방문처리 cnt +1 , 상하좌우에 대해서 재귀 
    else:
        # N-1, M-1 위치면 cnt 리턴
        dataList[row][col] = 0
        cnt += 1
        if(row == N-1 and col == M-1):
            print(cnt)
            return
        dfs(row+1, col, dataList, cnt)
        dfs(row-1, col, dataList, cnt)
        dfs(row, col+1, dataList, cnt)
        dfs(row, col-1, dataList, cnt)
    
# 매서드 실행
dfs(0,0,maze,0)
