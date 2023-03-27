"""해당하는 숫자가 숫자 리스트 안에 있는지 없는지 찾는 문제! 2초로 시간이 넉넉하므로 간단하게 in을 써서 풀어보자"""
import sys

N = int(input())
cards = set(list(map(int, sys.stdin.readline().strip().split())))
M = int(input())
targets = list(map(int, sys.stdin.readline().strip().split()))

result=[]
for i in range(M):
    if targets[i] in cards:
        result.append(1)
    else:
        result.append(0)
        
for i in range(M):
    print(result[i], end=" ")