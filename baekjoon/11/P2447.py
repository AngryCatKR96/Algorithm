"""별찍기! 일단 재귀문제다. 뭐부터 생각해? base condition!! base condition이 이 문제에서 뭔데? N=1!! 그럼 재귀에 필요한 변화는?
/3이겠지? 필요한 매개변수는? 빈칸 출력할 매개변수 필요할거같다. 그럼 일반화를 시키자면? 일단 N이 주어지면 
N/3 세번 출력
N/3한번 빈칸 한번출력
N/3세번출력
이거를 출력으로 할 생각을 하지말고 리스트로 해보자
return값이 뭐일지도 생각해야함!!"""
def star(n):
    if(n == 1):
        return ['*']
    
    starList = star(n//3) # 재귀 
    resultList = []
    for s in starList: # n=9일떄 statList의 길이는 3이고 ['***', '* *', '***'] 이므로 for 세번이니까 총 9행임
        resultList.append(s*3) # 첫행에 '***' 세번, 두번째 행에  '* *' 세번, 세번째 행에 '***' 세번... 이런 식으로
    for s in starList:
        resultList.append(s+ ' '*(n//3)+ s)
    for s in starList:
        resultList.append(s*3)    
    
    return resultList   
    

N = int(input())

print('\n'.join(star(N))) # 리스트 출력시 join을 활용하는 좋은 방법