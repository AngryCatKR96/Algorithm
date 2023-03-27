import sys, heapq

# 무한을 의미하는 값으로 10억 설정
INF = pow(10,9)

# 입력 받기
V, E = map(int, input().split())
K = int(input())

# 빈 연결 정보 리스트 생성 , graph
graph = [[] for _ in range(V+1)]

# 최단 거리 테이블 생성 및 초기화, distance
distance = [INF] * (V+1)

# 모든 간선 정보 입력 받기
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 메서드, dijkstra(start)
def dijkstra(start):
    # priority queue 생성
    pq = [] 
    
    # 시작 노드 초기화(자기 자신 거리 0 큐에 삽입, 시작 노드 거리 0)
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    # 큐가 비어있지 않다면
    while(pq):
        # 큐에서 현재 최단 거리가 가장 짧은 노드의 정보 꺼내기
        dis, now = heapq.heappop(pq)
        
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시(거리 비교 통해서 확인) 
        if distance[now] < dis:
            continue
        
        for i in graph[now]:
            cost = dis + i[1]
            # 현재 노드와 연결된 다른 노드를 확인 >> 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신(distance와 큐 모두 해줘야함)
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(pq, (cost, i[0]))
                
# 다익스트라 알고리즘 메서드 수행
dijkstra(K)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])    