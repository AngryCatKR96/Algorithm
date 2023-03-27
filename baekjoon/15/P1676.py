import math

N = int(input())

facto = math.factorial(N)

count = 0
while facto % 10 == 0:
    count += 1
    facto = facto // 10
    
print(count)
