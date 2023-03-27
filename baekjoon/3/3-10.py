import sys

input = sys.stdin.readline

count = 0
result = []

while True:
    A, B = map(int,input().split())
    
    if A == 0 & B== 0:
        break
    else: 
        count += 1
    
    result.append(A+B)
    
    
    
for i in range(count):
    print(result[i])
    
    