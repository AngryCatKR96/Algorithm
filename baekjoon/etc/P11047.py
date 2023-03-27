"""K원을 만드는데 필요한 최소한의 동전 개수를 찾기 위해선 먼저 
1) K값보다 작거나 같은 동전의 가치 중 최댓값을 찾는다
2) 그 최대값으로 나눈 몫은 개수에 추가하고 나머지로 다시 1) 반복
반복이기에 재귀를 활용할 수도 반복문을 활용할 수도 있다.
코드 자체는 재귀로 푸는 것이 깔끔하게 나올것이고 속도는 반복문이 빠를 것으로 예상
나누어 떨어지지 않는 경우를 테스트케이스로 준다는 말이 없었으므로 동전의 가치를 담는 리스트의 첫번째 요소로는 항상 나누어 떨어질 것이다.
따라서 base condition은 나누는 값이 첫번째 요소 일때! 
매개변수는 동전의 가치와 K일 것이고
N의 개수가 매우 많다면 탐색 과정에서 이진탐색(정렬되어있으므로)을 사용할 수도 있겠지만
최대 10개까지라고 하니 굳이? 싶다
구하는 값이 동전의 개수이므로 count를 전역변수로 선언하여 세주면 될것이고 return값은 딱히 필요 없으므로 void로 해도 충분할 것이다."""
# 재귀함수 coin 정의
def coin(inputList, money):
    global count
    for i in range(len(inputList)):
        j = len(inputList)-1-i
        if inputList[j] <= money:
            count += money // inputList[j]
            if money % inputList[j] == 0:
                return
            else: 
                coin(inputList, money % inputList[j])
                return
                
# 변수 초기화
count = 0    

# 인풋 받기
N, K = map(int, input().split())

coins = []
for _  in range(N):
    coins.append(int(input()))
    
# 매서드 실행 
coin(coins, K)

# 결과 출력
print(count)

    