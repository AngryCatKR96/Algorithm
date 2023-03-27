"""트리의 구조는 딕셔너리를 이용  -> 부모만 찾으면 되므로 value값에 부모 노드의 정보만 저장한다.
부모 자식 관계는 값이 dic의 key에 있다면 있는 값이 부모임
기존에 있는 값과 연결하는 것이 아닌 완전히 새로운 관계가 나올 수도 있음 >> 어떻게 해결하지"""
import sys

# N입력
N = int(input())

# 트리 생성 및 초기화
tree = {}
tree[1] = 0

# N-1번 실행
for _ in range(N-1):
    A, B = map(int,sys.stdin.readline().strip().split())
    # tree의 key값에 값이 있으면 없는 값을 key로, 있는 값을 value(부모노드)로 저장
    if A in tree:
        tree[B] = A
    else:
        tree[A] = B
        
# 2부터 순서대로 부모노드 출력
for i in range(2,N+1):
    print(tree[i])