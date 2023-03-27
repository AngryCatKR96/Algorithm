"""첫번째링의 반지름/N번째 링의 반지름 을 각각 둘의 최대공약수로 나누면된다"""
# 최대 공약수 메서드
def GCD(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
        
    rem = num1 % num2
    while rem != 0:
        num1 = num2
        num2 = rem
        rem = num1 % num2
    return num2
        
N = int(input())
rings = list(map(int,input().split()))

# 몇바퀴도는지 출력
for i in range(1,N):
    gcd = GCD(rings[0],rings[i])
    print("%d/%d" % (rings[0]//gcd,rings[i]//gcd))
    
