# 골드바흐의 추측
# 2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
# 골드바흐 파티션이 여러 가지일 경우에는 두 소수의 차이가 가장 작은 것을 출력

# 일단 에라토스테네스의 체로 소수부터 만든다!
# 짝이 있으면 거기서 끝!
# 없을리는 없으므로 예외 처리는 X

# 에라토스테네스의 체
def prime(N):
    sieve = [True]*(N+1) # 여기 N+1해주는건 index를 N까지 만들기 위해
    for i in range(2,int(N**0.5) +1): # 여기 +1해주는건 range가 이상,미만이기 때문
        if sieve[i] == True:
            for j in range(i*2,N+1,i): 
                sieve[j] = False
                
    return [i for i in range(2, N+1) if sieve[i] == True ] 



# T 받기
T = int(input())

list_N = []
list_result = []

# N 받기
for _ in range(T):
    list_N.append(int(input()))

# N 중에 maxN 찾아서 소수 리스트 만들기
maxN = max(list_N)
list_prime = prime(maxN)

# 테스트 케이스 순서대로 리스트에서 테스트 케이스의 절반부터 비교해가며 소수 찾기
# 테스크케이스 - 소수 = 소수면 통과! 아니면 다른 소수! 이중 리스트로 저장
for i in range(len(list_N)):
    for j in range(len(list_prime)-1,-1,-1):
        try:
            if list_prime[j] <= int(list_N[i]*0.5):
                if list_N[i] - list_prime[j] in list_prime:
                    list_result.append([list_prime[j], list_N[i] - list_prime[j]])
                    break
                else:
                    continue
        except:
            continue

# 출력
for i in range(len(list_N)):
    print(list_result[i][0], end=" ")
    print(list_result[i][1])

