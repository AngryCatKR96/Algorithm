import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)# 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21 # 2^20 = 1,000,000, 최대 노드 수

# 노드 개수 입력
N = int(input())
# 부모 노드 정보(2차원 리스트)
parent = [[0]*LOG for _ in range(N+1)]
# 각 노드 까지의 깊이
d = [0] * (N+1)
# 각 노드의 깊이가 계산되었는지 여부
c = [False] * (N+1)
# 그래프 정보
graph = [[] for _ in range(N+1)]

# 간선 정보 입력(index가 노드의 번호, index에 있는 값들은 연결된 노드의 번호)
for _ in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수 dfs(x, depth)
def dfs(x, depth):
    # 노드 깊이 여부 갱신
    c[x] = True
    # 깊이 갱신
    d[x] = depth
    # x와 연결된 모든 노드(y) 검사
    for y in graph[x]:
        # 이미 깊이를 구했다면 넘기기
        if c[y] == True:
            continue
        # 안구했으면 부모 노드 갱신(2^0번 째 부모부터 갱신)
        parent[y][0] = x
        # 깊이 1 증가시키고 y에 대해서 재귀 실시
        dfs(y,depth+1)

 
# 전체 부모 관계를 설정하는 함수 set_parent()
def set_parent():
    # 루트 노드는 1번 노드
    dfs(1, 0)
    # 모든 노드에 대하여 2의 제곱꼴로 건너뛰었을 떄의 부모를 설정
    for i in range(1,LOG):
        for j in range(1,N+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수 lca(a,b)
def lca(a,b):
    # B가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이가 동일하도록 깊이 차이를 확인한 뒤, 깊이차이가 충분히 크다고하면 2의 제곱꼴만큼 감소하도록해서 깊은 쪽의 깊이가 감소하도록 만듬(시프트 연산자 이용)
    for i in range(LOG-1,-1,-1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록, 
    if a == b:
        return a
    #  노드가 같아질 때까지 양쪽의 조상을 하나씩 거슬러 올라감(2의 제곱 형태에서 큰값부터 작은값으로)
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상 리턴
    return parent[a][0]

# 전체 부모 관계 설정
set_parent()

# 시행 횟수 m 입력 받기
M = int(input())

# 각 시행마다 공통 조상 출력 
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a,b))