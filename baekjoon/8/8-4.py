# 에라토스테네스의 체(M이상 N이하)
def prime(M, N):
    sieve = [True]*(N+1) # N이 인덱스로 들어가므로 N+1을 곱해주어야 index 0을 포함해서 index N까지 만들어진다
    sieve[1] = False
    
    for i in range(2,int((N+1)**0.5) +1):
        if sieve[i] == True:
            for j in range(i*2,N+1,i):
                sieve[j] = False
                
    return [i for i in range(M, N+1) if sieve[i] == True ] # 결국에 소수 리스트의 요소가 되는건 index 값임.

M, N = map(int, input().split())

primes = prime(M, N)


for i in primes:
    print(i)