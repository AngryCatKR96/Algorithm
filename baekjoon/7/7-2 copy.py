# 육각형이다 > 주위에 6개 부착가능 
# 1 6 12 18 24 >> 차이가 6인 등차수열임
#  1 7 19 37 61 >> 합
# 일반항 B(n) = 6*(n-1) (n=2,3,4..)
# 합 일반항 S(n+1) = S(n) + 6*n
# S(1) = 1

def S(n):
    if n == 1:
        return 1
    else:
        ans = 1
        for i in range(1, n+1):  # 재귀함수 사용안했으나 이번에는 시간 초과 뜸...
            ans += 6*(i-1)       # 점화식이 아닌 일반항을 손으로 구해서 함수로 만들면 빠를거같다.
        return ans

N = int(input())

n=0

while True: 
    n += 1
    if N <= S(n+1) and N > S(n):
        print(n+1)
        break
    
