def bino_coef(n, k):
    if k==0 or n==k:
        return 1
    
    return bino_coef(n-1,k) + bino_coef(n-1,k-1)

N, M = map(int,input().split())

result = bino_coef(N,M)

count = 0
while result % 10 == 0:
    count += 1
    result = result // 10
    
print(count)