# 한자리 수는 무조건 한수이다 
# 두자리 수는 무조건 한수이다 > 수가 두개밖에 없기 때문에 차가 하나라서 비교할게 없다
# 세자리수 100부터는 차이가 같은지 확인해야 한다
# 100 > 차이 1, 0  > 다름 > 한수 아님
# 123 > 차이 1, 1 > 한수임
# 210 > 차이 1, 1 > 한수임
# 420 > 차이 2, 2 > 한수임
# 432 > 차이 1, 1 > 한수임
# 첫번째 케이스를 살펴보자. 1~110에서 한수의 개수
# 1~99 + 100에서 한수없음 = 99개

str_Num = input()
int_Num = int(str_Num)
list_Num = list(map(int,str_Num))

count = 0

if len(str_Num) == 1:
    count = int_Num
elif len(str_Num) == 2:
    count = int_Num
elif len(str_Num) >= 3:
    count += 99
    for j in range(100,int_Num+1):
        list_diff = []
        str_j = str(j)
        for i in range(len(str_j)):
            try:
                diff = int(str_j[i]) - int(str_j[i+1]) # i+1 이 마지막에 범위를 초과하기 때문에 오류처리가 필요
                list_diff.append(diff)
            except:
                pass
        
        if len(set(list_diff)) == 1:
            count += 1
            
print(count)