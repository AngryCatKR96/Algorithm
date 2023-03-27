import sys

input = sys.stdin.readline

T = int(input())

result = []

for i in range(T):
    A, B = map(int,input().split())
    result.append(A+B)
    
for i in range(T):
    print("Case #%d: %d" % (i+1,result[i]))