#베르트랑 공준
# n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다.
# 소수의 개수를 구하는 프로그램
# 결국 소수 개수 구하는 것이므로 에라토스테네스의 체 사용 가능!

# 에라토스테네스의 체(N초과 2N이하)
def prime(N):
    sieve = [True]*(2*N+1) 
    sieve[1] = False
    
    for i in range(2,int((2*N+1)**0.5) +1):
        if sieve[i] == True:
            for j in range(i*2,2*N+1,i):
                sieve[j] = False
    count = 0           
    for i in range(N+1, 2*N+1):
        if sieve[i] == True:
            count+=1
    return count

# 여러개의 테스트 케이스 입력(0 받으면 끝) -> 리스트에 결과 저장
result = []
while True:
    N = int(input())
    
    if N != 0:
        result.append(prime(N))
    else:
        break
    
# 결과 출력

for i in range(len(result)):
    print(result[i])
