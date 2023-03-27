import sys

input = sys.stdin.readline

count = 0
result = []

while True:
    try:
        count += 1
        A, B = map(int,input().split())
        result.append(A+B)
    except:
        break
    
for i in range(count-1):
    print(result[i])