import sys

N = int(input())

inputList = list(map(int,sys.stdin.readline().strip().split()))

print(min(inputList)*max(inputList))