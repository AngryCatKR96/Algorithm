"""세변의 길이가 랜덤으로 입력 > 직각 삼각형인지 아닌지 판단하는 문제 
그냥 너무 간단하게 가장 큰 변의 길이 c와 나머지 변의 길이 a,b가 있을 떄 c^2= a^2 + b^2만 체크해주면되는 너~무 쉬운문제"""
# 입력받으면서 동시에 출력
while(True):
    A, B, C = map(int, input().split())
    if(A==0):
        break
    tri= [A,B,C]
    tri.sort()
    if(pow(tri[2],2) == pow(tri[0],2) + pow(tri[1],2)):
        print('right')
    else:
        print('wrong')
    