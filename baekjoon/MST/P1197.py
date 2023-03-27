import sys

# find_parent
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union_parent
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(유니온 연산)의 개수 입력 받기
V, E = map(int,input().split())

# 부모테이블 0으로 초기화
parent = [0] * (V+1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블 상에서 부모를 자기 자신으로 초기화
for i in range(1,V+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(E):
    # 비용 순으로 정렬하기 위해서 튜플의 첫번째 원소를 비용으로 설정
    A, B, cost = map(int, sys.stdin.readline().strip().split())
    edges.append((cost, A, B))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩으로 확인하며
for edge in edges:
    cost, A, B = edge
    # 사이클이 발생하지 않는 경우(서로 다른 부모를 가지고 있을 때)에만 집합에 포함(유니온 연산 시행, 결과값에 코스트 더하기)
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += cost
        
print(result)