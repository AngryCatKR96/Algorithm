"""N개의 수를 M으로 나누었을 때 나머지가 모두 같은 M을 찾는 문제
일단 간단하게 생각하면 브루트 포스로 풀면된다. N개의 수를 2부터 1씩 증가시키며 가장 작은 수보다 작은 수까지 나눠본다.
최악의 경우 100개의 1,000,000,000이 주어질수 있으므로 시간 초과가 날 거 같다. >> 그래도 일단 해보자"""
import sys

N = int(sys.stdin.readline().strip())

inputList = []
for _ in range(N):
    inputList.append(int(sys.stdin.readline().strip()))
    
# for문으로 나머지 구하기
m = max(inputList)
result = []
for i in range(2,m+1):
    rem = m % i
    for j in range(len(inputList)):
        if inputList[j] % i != rem:
            break
        if j == len(inputList)-1:
            result.append(i)

for i in result:
    print(i, end= " ")

