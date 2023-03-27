"""다리 놓기 문제 : M개 사이트중 N개를 고르는 경우의 수를 구하시오
시간제한 -> 0.5초 -> DP를 사용하면 시간 초과 날듯 -> 일단 해보고 시간 초과 나면 팩토리얼을 이용한 계산식을 쓰자
-> DP써도 되네? -> 테스트케이스가 적어서 그럼!"""
import sys

def bino_coef(n,k):
    if n < k:
        return 0
    
    cache = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    
    def choose(times, got):
        if times == n:
            return got == k
        
        if cache[times][got] != -1:
            return cache[times][got]
        
        cache[times][got] = choose(times+1,got) + choose(times+1,got+1) 
        return cache[times][got]
    
    return choose(0,0)


T = int(input())

for _ in range(T):
    N, M = map(int,sys.stdin.readline().strip().split())
    
    print(bino_coef(M,N))