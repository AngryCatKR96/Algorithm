import sys

# 런타임 오류 피하기
sys.setrecursionlimit(10**6)

# 노드 개수 입력
N = int(input())

# 부모 노드 정보
parent = [0] * (N+1)
# 각 노드 까지의 깊이
d = [0] * (N+1)
# 각 노드의 깊이가 계산되었는지 여부
c = [False] * (N+1)
# 그래프 정보
graph = [[] for _ in range(N+1)]

    
# 간선 정보 입력(index가 노드의 번호, index에 있는 값들은 연결된 노드의 번호)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수 dfs(x, depth)
def dfs(x, depth):
    # 노드 깊이 여부 갱신
    c[x] =  True
    # 깊이 갱신
    d[x] = depth
    # x와 연결된 모든 노드(y) 검사
    for y in graph[x]:
        # 이미 깊이를 구했다면 넘기기
        if c[y] == True:
            continue
        # 안구했으면 부모 노드 갱신
        parent[y] = x
        # 깊이 1 증가시키고 y에 대해서 재귀 실시
        dfs(y, depth+1)

# A와 B의 최소 공통 조상을 찾는 함수 lca(a,b)
def lca(a,b):
    # 먼저 깊이가 동일할 때까지 더 깊은 쪽의 조상을 하나씩 거슬러 올라감
    while d[a] != d[b]:
        if d[a] < d[b]:
            b = parent[b]
        else:
            a = parent[a]
    # 이후, 노드가 같아질 때까지 양쪽의 조상을 하나씩 거슬러 올라감
    while a != b:
        a = parent[a]
        b = parent[b]
    # 같으면 리턴
    return a

# 루트 노드는 1번노드, dfs 실행시켜서 모든 노드의 깊이 리스트 갱신
dfs(1, 0)

# 시행 횟수 m 입력 받기
M = int(input())

# 각 시행마다 공통 조상 출력 
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(lca(a,b))
    