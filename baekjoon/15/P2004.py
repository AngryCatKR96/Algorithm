def bino_coef(n, m):
    if n < m:
        return 0
    
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def choose(times, got):
        if times == n:
            return got == m
        
        if cache[times][got] != -1:
            return cache[times][got]
        
        cache[times][got] = choose(times+1,got) + choose(times+1,got+1)
        return cache[times][got]
    
    return choose(0,0)
    
N, M = map(int,input().split())

result = bino_coef(N, M)

count = 0
while result % 10 == 0:
    count += 1
    result = result // 10
    
print(count)