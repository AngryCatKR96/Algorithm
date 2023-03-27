"""그냥 단순하게 교집합 구하는 문제인듯?"""
import sys
# N,M 입력
N, M = map(int, input().split())

# 듣못 집합, 보못 집합 선언
notHeard = set()
notSaw = set()

# 집합 채우기
for _ in range(N):
    notHeard.add(sys.stdin.readline().strip())

for _ in range(M):
    notSaw.add(sys.stdin.readline().strip())
    
# 정렬된 교집합 리스트 구하기
notHeardSaw = sorted(list(notHeard & notSaw))

# 요소 하나씩 출력
print(len(notHeardSaw))
for i in notHeardSaw:
    print(i)
