# 에라토스테네스의 체
def prime(N):
    sieve = [True]*N
    for i in range(2,int(N**0.5) +1):
        if sieve[i] == True:
            for j in range(i*2,N,i):
                sieve[j] = False
                
    return [i for i in range(2, N) if sieve[i] == True ]

# 소인수분해 메소드
def facto(N):
    if N == 1:
        pass
    else:
        primes = prime(N)
        count = 0
        for i in primes:
            while N % i == 0:
                count += 1
                N /= i
                print(i)
        if count == 0:
            print(N)

N = int(input())

facto(N)

        

    
    