"""최대공약수와 최소공배수 
최대공약수란 두 수의 약수 중에서 가장 큰 약수
최소공배수란 두수의 배수 중에서 가장 작은 배수
찾기 -> 두 수를 두 수보다 작은 소수로 2부터 차근차근 나눠봄 -> 나눠서 나머지 0이면 나누고 
-> 몫값을 두 수로 갱신 -> 다시 2부터 시도 -> 안나눠지면 더 큰 소수로 나눠봄 -> 소수가 두 수보다 커질 때까지 시도
-> 없으면 끝. -> 지금 까지 시도 했던 소수들의 곱이 최대공약수, 최대공약수*남은 두수의 곱 이 최소 공배수
그럼 일단 소수로 이루어진 리스트부터 구해야겠네? 에라토스테네스의 체!"""
def prime(limit):
    checkList = [True for _ in range(limit+1)]
    num = 2
    while(num<limit+1):
        if checkList[num] == True:
            for i in range(num*2,limit+1,num):
                checkList[i] = False
        num += 1
    return [i for i in range(2,limit+1) if checkList[i]==True]
    
N, M = map(int,input().split())

primeList = prime(10000)

# 약수 리스트 만들기
index = 0
aliquot = [] # 약수들의 리스트
while(index < len(primeList)):
    if N % primeList[index] == 0 and M % primeList[index] == 0:
        N = N//primeList[index]
        M = M//primeList[index]
        aliquot.append(primeList[index])
    else:
        index += 1
  
# 최대 공약수      
GCD = 1
for i in aliquot:
    GCD *= i
    
# 최대 공배수 
LCM = GCD*N*M

# 출력
print(GCD)
print(LCM)
