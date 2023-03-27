"""중복을 허용하지 않기 떄문에 set을 쓰면될거같긴한데 부분문자열 자체를 구하는데 시간이 많이 걸리지 않을까? for문을 한번 써보자
그리고 in으로 집합 안에 있는지 확인하고 add하는게 나을까 아니면 그냥 어차피 중복 허용안하니까 바로 add하는게 좋을까"""

string =  input()

subString = set()

# for문 으로 부분 문자열 구하기
for length in range(0,len(string)): # 길이 1인 부분 문자열부터 길이 5인 부분 문자열까지 비교할거임
    # 길이가 1 길어질수록 탐색 범위도 1씩 줄어듬 
    for start in range(0,len(string)-length):
        subString.add(string[start:start+length+1])
        
print(len(subString))