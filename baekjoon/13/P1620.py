"""포켓몬의 해당하는 번호 -> index나 딕셔너리의 key이용 -> 탐색 속도 고려하면 딕셔너리가 맞는데 key -> value는 쉽게 찾아도
value -> key는 어떻게 찾지?
key와 value를 반전시킨 딕셔너리를 새로 만들어서 찾자"""
import sys

# 데이터 입력
N, M = map(int,input().split())

PokeDict = dict()
for i in range(N):
    PokeDict[i+1] = sys.stdin.readline().strip()
    
rev_PokeDict = {v:k for k,v in PokeDict.items()}

# 문제 입력 및 출력
for _ in range(M):
    try:
        target = sys.stdin.readline().strip()
        int_target = int(target)
    except:
        print(rev_PokeDict.get(target))
    else:
        print(PokeDict.get(int_target))

