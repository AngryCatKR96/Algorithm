"""백트래킹 문제 >> base condition이 존재. checked 필요.
일단 한명씩 고르는데 총 N/2명 골랐으면 끝, count와 sum은 전역변수가 되어서는 안됨. 매개변수 값으로 넘겨주자
count라는 매개변수를 만들지 말고 함수 자체를 총n명의 사람 중 현재 k명의 사람을 골랐고 """
import sys

# 입력
N = int(input())

# 변수 정의
power = []
visited = [False for _ in range(N)]
minDiff = 100000

# 능력치 입력
for _ in range(N):
    power.append(list(map(int, sys.stdin.readline().strip().split())))

# N명 중 N/2명을 고르기 위한 메서드, 현재 k명을 골랐음
def DFS(k, i):
    global minDiff
    if k == N//2: # 탈출 조건
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] == True and visited[j] == True: start += power[i][j]
                if visited[i] == False and visited[j] == False: link += power[i][j]
        diff = abs(start-link)
        if diff < minDiff:
            minDiff = diff
        return
    
    else:
        for j in range(i, N): 
            if visited[j] == False:
                visited[j] = True
                DFS(k+1, j+1)  
                visited[j] = False  
    return          
    

# 메서드실행 
DFS(0,0)

print(minDiff)