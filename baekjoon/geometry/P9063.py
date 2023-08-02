import sys

input = sys.stdin.readline

N = int(input())

xList = []
yList = []


for _ in range(N):
    X, Y = map(int, input().split())

    xList.append(X)
    yList.append(Y)

if N == 1:
    print(0)
else:
    maxX = max(xList)
    minX = min(xList)
    maxY = max(yList)
    minY = min(yList)

    if maxX == minX or maxY == minY:
        print(0)
    else:
        print((maxX-minX)*(maxY-minY))
