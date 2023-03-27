# 육각형이다 > 주위에 6개 부착가능 
#   6 12 18 24 >> 계차수열 차이가 6
#  1 7 19 37 61 >> 원래 수열
# 일반항 B(n) = 6*(n-1) (n=2,3,4..)
# 합 일반항 S(n+1) = S(n) + 6*n
# S(1) = 1
# 함수를 사용하지말고 해보자
# 각 합의 항에서 1빼고 6으로 나누면
# 0 1 3 6 10     

import sys

input = sys.stdin.readline

def S(n):
    if n == 1:
        return 1
    else:
        return 1 + (n-1)*6 + (n-1)*(n-2)*3

N = int(input())

n = 1

while True:  # 함수를 한 번만 계산하는 방법, 함수값을 변수에 저장하면 같은 계산을 두번할 필요가 없다.
    if S(n) >= N:
        print(n)
        break
    n += 1
    
#while True:
#    if N <= S(n+1) and N > S(n):   # 함수를 두번 계산해서 시간이 더 걸림
#        print(n+1)
#        break
#    n += 1
    
