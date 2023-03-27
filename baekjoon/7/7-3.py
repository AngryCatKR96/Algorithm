# 수열로 한번 풀어보자!
# 각 대각선 별 갯수 1 2 3 4 5 ... 차이를 1로 가지는 등차수열
# 1 3 6 10 .... 
#  2 3 4 계차수열
import sys

def S(n): # 계차수열의 원래 수열의 합 
    if n == 1:
        return 1
    else:
        return 1 + (n-1)*2 + (n-1)*(n-2)*0.5
    
N = int(sys.stdin.readline())

n = 1
while S(n) < N:  # 합이 N보다 커질 때의 n값을 찾는 과정, n값은 몇 번째 대각선인지를 의미한다.
    n += 1
    
    
if n % 2 == 0:  # n이 짝수라면 위에서부터 내려오며 찾고
    x = N - S(n-1)
    y = n-x+1
elif n % 2 == 1:  # n이 홀수라면 아래에서부터 올라오며 찾는다
    y = N - S(n-1)
    x = n-y+1
     
            
    
print(str(int(x))+"/"+str(int(y)))