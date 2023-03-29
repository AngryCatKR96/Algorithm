from collections import deque
import sys
input = sys.stdin.readline

# 노드의 개수와 간선의 개수 입력 받기
N, M = map(int, input().split())

# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0]*(N+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for _ in range(N+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(M):
    # 정점 A에서 B로 이동 가능
    a, b = map(int, input().split())
    graph[a].append(b)
    # 진입 차수를 1 증가
    indegree[b] += 1

# 위상 정렬 함수 topology_sort()
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result = []
    # 큐 기능을 위한 deque 라이브러리 사용
    q = deque()
    # 처음 시작할 떄는 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때까지 반복  
    while q:
        # 큐에서 원소 꺼내기, 꺼내는 순서가 정렬 결과
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입 차수가 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
            
    # 위상정렬을 수행한 결과 출력
    for i in result:
        print(i, end=" ")

# 위상정렬 메서드 실행
topology_sort()