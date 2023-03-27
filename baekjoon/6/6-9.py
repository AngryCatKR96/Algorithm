S = input()

cr_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count = len(S)

for i in cr_alphabet:
    if S.find(i) == -1:
        pass
    else:
        count = count - S.count(i) 
        
# 두번 있는건 어떻게 세지? > count를 replace보다 먼저 넣어주면 됨.
# S = S.replace(i,"")  # replace가 안먹힌다 왜 이럴까? > replace는 append처럼 자동 저장이되는게 아니라 값을 반환하기 때문에 변수를 설정해줘야한다
# replace는 한번에 모든 i를 바꿔버리므로 두개 이상이 있어도 바꿔버림
# 예제 입력3 처럼 중간에 크로아니아 알파벳이 지워지고 양쪽의 알파벳이 합쳐서 크파벳이 된다면 또 카운팅됨

# (최종) count를 더하는 것보다 전체에서 빼주는게 나을 때도 있음. 
# 이번 문제 같은 경우 replace를 사용하면 예제 3에서 nljj에서 lj를 빼면 nj가 되어서 한번 더 카운팅되므로
# replace를 사용하는 것은 바람직하지 않음
# 따라서 전체 길이에서 크파벳 수 만큼 -1해주는 것이 이상적임 
        
print(count) 


        