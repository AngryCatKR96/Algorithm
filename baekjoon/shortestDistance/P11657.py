import sys

# 무한을 의미하는 값으로 10억 설정 int(1e9)
INF = int(1e9)

# 벨만 포드 알고리즘 메서드
def bp(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    
    # 전체 n 번의 라운드 반복
    for i in range(N):
        # 매 반복마다 모든 간선을 확인하며
        for j in range(M):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + cost:
                distance[next_node] = distance[cur_node] + cost
                # n번 째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == N-1:
                    return True
    return False
            
# 노드의 개수, 간선의 개수를 입력 받기
N, M = map(int,input().split())
  
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF for _ in range(N+1)]

# 모든 간선 정보 입력 받기
for _ in range(M):
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    A, B, C = map(int, sys.stdin.readline().strip().split())
    edges.append((A,B,C))

# 벨만 포드 알고리즘 수행
# 1번 노드가 시작 노드
neg_cycle = bp(1)

# 음수 순환이 존재하는지 안하는지 체크
if neg_cycle == True:
    print(-1)
# 1번 노드를 제외한 다른 노드로 가기 위한 최단 거리 출력
else:
    for i in range(2,N+1):
        # 도달할 수 없는 경우 -1 출력
        if distance[i] == INF:
            print(-1)
        # 도달할 수 있는 경우 거리 출력
        else:
            print(distance[i])
    



