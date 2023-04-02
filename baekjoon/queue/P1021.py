import sys
from collections import deque

input = sys.stdin.readline

# N, M 입력받기
N, M = map(int,input().split())

# 뽑아 내려는 수 입력 받기
nums = list(map(int,input().split()))

# deque 생성 및 초기화
dq = deque()
for i in range(N):
    dq.append(i+1)

# 변수 count 초기화
count = 0

# 뽑아 내려는 수의 위치를 디큐에서 찾기
for num in nums:
    # 앞에서 가까운지 뒤에서 가까운지 판별 
    where = dq.index(num) 
    # 더 가까운 쪽에서 rotate 실행(카운트 증가)해서 큐의 0번째 인덱스로 옮기고 뽑아내기
    if where <= (len(dq)-1)//2:
        dq.rotate(-where)
        count += where
        dq.popleft()
        
    else:
        dq.rotate(len(dq)-where)
        count += len(dq)-where
        dq.popleft()
 

# 카운트 출력
print(count)