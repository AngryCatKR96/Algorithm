S = input().upper()

alphabet = set(S)
dic = {}

for i in alphabet:
    count = S.count(i)
    dic[i] = count # key가 중복되는지 안되는 확인
    
list = list(dic.values()) # dic.values()는 리스트가 아니다! 리스트로 변환시켜줘야함

max = max(list)    

if list.count(max) == 1: # max 함수는 최대값이 두개 이상일때는 하나만 나온다.
    print([k for k, v in dic.items() if v == max][0]) # value로 key 찾기 list comprehension을 사용함
else:
    print('?')