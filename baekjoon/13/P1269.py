"""대칭 차집합 = 결국 합집합에서 교집합 뺀거 아님?"""
import sys

numA, numB = map(int, input().split())
A = set(map(int,sys.stdin.readline().strip().split()))
B = set(map(int,sys.stdin.readline().strip().split()))

# 합집합 - 교집합
result = (A | B) - (A & B)

print(len(result))