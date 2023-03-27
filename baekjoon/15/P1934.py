"""유클리드 호제법, A,B의 최대 공약수는 C=A%B와 B의 최대 공약수와 같다."""
import sys

T = int(input())

for _ in range(T):
    A, B = map(int,sys.stdin.readline().strip().split())
    ini  = [A, B] # 초기값 저장
    if A<B: # 무조건 A>B로 세팅되게
        A, B = B, A
        
    C = A%B
    while C != 0:
        A = B
        B = C
        C = A % B
    
    print(ini[0]*ini[1]//B)
    