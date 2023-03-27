# input 받기
N = int(input())
numbers = list(map(int,input().split()))

# 변수 선언
count = 0 # 소수가 아닌 애들을 카운팅

# 반복문을 이용하여 각 수(Num)가 소수인지 검사(브루트 포스로 1부터 Num-1까지 다 나눠서) & 소수면 카운팅
for num in numbers:
    if num == 1: # index error 방지
        count += 1
        continue
    
    for i in range(1, num):
        if i != 1 and num % i == 0: # 소수가 아닐 때 찾으면 바로 break
            count += 1
            break
        elif i != 1 and num % i != 0: 
            continue
        elif i == 1:
            continue
            
     
# 카운팅 출력
print(N - count)   