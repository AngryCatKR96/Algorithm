# 그룹단어의 개념은 이해완료! 
# 어떻게 그룹단어인지를 확인할까?
# 각 문자가 연속되지 않고 하나라도 떨어져서 나오면 그룹단어가 아님
# 떨어져서 > 가 포인트인거같은데 어떻게 떨어져있는지를 확인할 수 있을까
# 일단 떨어져있다는 것은 위치와 관계있는 이야기임
# 슬라이싱을 활용해서 i번째 문자가 i+2번째 이후의 문자열에 있는지 확인
# 있으면 그룹단어 아님!
# i+2 번째 오류 조심 

N = int(input())

count = N

for _ in range(N):
    
    S = input()
    
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            pass
        elif S[i] in S[i+1:]:
            count -= 1
            break
        
print(count)
        