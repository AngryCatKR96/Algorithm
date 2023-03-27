import sys
sys.setrecursionlimit(10**6)

#특정 원소가 속한 집합을 찾는 메서드 find_parent
def find_parent(parent, x):
#루트 노드가 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parent(parent , parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치는 메서드 union_parent
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    # 루트 노드 찾아서 더 큰쪽이 더 작은 쪽에 합쳐짐 == 루트 노드 갱신
    if a < b: 
        parent[b] = a
    else:
        parent[a] = b
        


# 노드의 개수와 간선(유니온 연산)의 개수 입력 받기
n, m = map(int,input().split())

# 부모 테이블 0으로 초기화
parent = [0] * (n+1)

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(n+1):
    parent[i] = i
    
# 유니온 연산 각각 수행
for _ in range(m):
    c, a, b = map(int,sys.stdin.readline().strip().split())
    
    if c == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")