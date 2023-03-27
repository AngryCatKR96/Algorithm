import math

facto = math.factorial

N, M = map(int,input().split())

result = facto(N)/(facto(N-M)*facto(M))

count = 0
while result % 10 == 0:
    count += 1
    result = result // 10
    
print(count)