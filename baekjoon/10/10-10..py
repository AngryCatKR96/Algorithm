import sys
# 길이로 정렬하는 메서드, 삽입 정렬 기반
def stringSort(list):
    index = 0
    prev = 0
    for index in range(1,len(list)):
        temp = list[index]
        tempLength = len(list[index])
        prev = index - 1
        while prev>=0 and tempLength <= len(list[prev]): 
            if tempLength == len(list[prev]):
                temp, list[prev] = alphaSort(temp, list[prev])
            list[prev+1] = list[prev]
            prev -= 1
        list[prev+1] = temp
        
    return list

# 알파벳 순으로 정렬하는 메서드
def alphaSort(str1, str2):
    # string의 index를 사용해 하나하나 비교(아스키코드값 사용) for문 사용
    for i in range(len(str1)):
        if ord(str1[i]) > ord(str2[i]):
            return str2, str1
    return str1, str2
            

# N 입력
N = int(sys.stdin.readline().strip())

# 리스트에 저장
inputList = []
for _ in range(N):
    inputList.append(sys.stdin.readline().strip())
    
# 길이로 정렬
stringSort(inputList)

# 길이 같으면 알파벳 순으로 정렬, String의 [0]비교하고 또 같으면 [1]비교하고.. 하는 식으로

# 출력
for i in inputList:
    print(i)