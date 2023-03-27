# 육각형이다 > 주위에 6개 부착가능 
# 1 6 12 18 24 >> 차이가 6인 등차수열임
#  1 7 19 37 61 >> 합
# 일반항 B(n) = 6*(n-1) (n=2,3,4..)
# 합 일반항 S(n+1) = S(n) + 6*n
# S(1) = 1

def S(n):
    if n==1:
        return 1
    else:
        return S(n-1) + 6*(n-1) # NoneType Error 발생 >> return을 넣어주지 않았기 때문

N = int(input())

n=0

while True:
    n += 1
    if N <= S(n+1) and N > S(n):
        print(n+1)
        break
    
# RecursionError 발생! 재귀함수의 깊이 때문에 발생한다고 한다.