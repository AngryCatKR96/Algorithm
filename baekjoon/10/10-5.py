import sys

#카운팅 정렬(배열)
# def countingSort(list):
#     count = [0]*(max(list)+1)
#     result = [0]*len(list)
    
#     for i in list:
#         count[i] += 1
        
#     for i in range(1,len(count)):
#         count[i] += count[i-1]
        
#     for i in list:
#         result[count[i]-1] = i
#         count[i] -= 1
        
#     return result

#카운팅 정렬(딕셔너리)
# def countingSort(list):
#     count = {}
#     for num in list:
#         if num in count:
#             count[num] += 1
#         else:
#             count[num] = 1
            
#     result = []
    
#     for num in range(max(list) + 1):
#         while num in count and count[num] != 0:
#             result.append(num)
#             count[num] -= 1
            
#     return result
        
# 개수 N
N = int(sys.stdin.readline())

count = [0]*(10001)

# 입력
for _ in range(N):
    inputNum = int(sys.stdin.readline())
    count[inputNum] += 1
    
for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
