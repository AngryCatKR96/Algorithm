"""재귀 문제, base condition은? N=1일때 별 하나 출력, 매개변수는 N하나
return 타입은 리스트★★★★★★★★중요
return한 리스트를 한줄씩 (어차피 출력은 한줄씩 하므로)"""

def star(n):
    if(n==1):
        return ['*']
    
    starList = star(n//3)
    resultList = []
    for s in starList: # n=1일때 list는 1행, n=3일떄 리스트는 3행, n=9일떄 리스트는 9행으로 점점 늘어나므로 starList의 길이도 점점 길어짐
        resultList.append(s*3) 
    for s in starList:
        resultList.append(s + ' '*(n//3) + s)
    for s in starList:
        resultList.append(s*3)
        
    return resultList

# 인풋
N = int(input())

# 메서드 실행
result = star(N)

# 출력
print('\n'.join(result))
