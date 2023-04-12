N, K = map(int,input().split())

result = 0
count = 0
for i in range(1,N+1):
    if N % i == 0:
       count += 1
       if count == K:
           result = i
           break 
       
if count != N:
    print(result)
else:
    print(0)