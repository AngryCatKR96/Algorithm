# input 받기
M = int(input())
N = int(input())

# 변수 선언
min = 0 # 최솟값
sum = 0 # 소수의 합

# 반복문을 이용하여 M부터 N까지의 모든 자연수를 소수인지 검사(브루트 포스로 1부터 Num-1까지 다 나눠서) & 소수면 카운팅
for num in range(M,N+1):
    if num == 1: # index error 방지
        continue
    
    
    for i in range(1, num):
        if i != 1 and num % i == 0: # 1이 아닌 인수가 존재한다 == 소수가 아니다 => 이번 num은 더 계산할 이유 없음
            break
        elif i != 1 and num % i != 0: # i가 인수가 아닐 때
            if i != num-1: # i가 num-1이 아니면 현재의 i보다 큰 i가 인수일 수도 있으므로 다음 사이클로 넘어간다
                continue
            else: # i가 num-1이면 1을 제외한 인수가 없다는 것이므로 num은 소수임!
                if sum == 0: # sum이 0이다. 는 이번 num이 처음 찾은 소수라는 뜻
                    min = num
                sum += num
                break
        elif i == 1 and num != 2:
            continue
        elif i == 1 and num == 2:
            min = 2
            sum += 2
            
     
# 최소 소수와 합 출력
if sum == 0: # 합이 0이다.는 찾은 소수가 없다는 뜻
    print(-1)
else: 
    print(sum)
    print(min) 