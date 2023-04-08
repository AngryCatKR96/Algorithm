"""백트래킹 문제!! 어떻게 최댓값과 최솟값을 구할까? 
백트래킹이므로 base condition을 생각해봐야겠지? 백트래킹은 일단 기본적으로 완전 탐색이고 최댓값과 최솟값을 갱신하는 식으로 가야 할거같아
base contion이 최신 최댓값과 최솟값이 아닐까??
그리고 내가 해당 연산자를 사용했는지 안했는지도 따져야하니까 사용하면 횟수를 마이너스 해줄까? 근데 연산자의 조합을 따져야하잖아
조합을 따지는데에서 백트래킹이 사용되는건가? 그럼 조합에서 백트래킹이 사용되고 최댓값 최솟값 비교하는데에서 탈출하는건 또 따로인가? 근데 어차피 완전 탐색해야하니 갱신만 해주고
메서드를 종료할 필요는 없네!
자 그럼 조합을 만드는데에서 백트래킹을 사용한다고 치자 for문으로 돌아가면서 모든 경우의 수를 탐색하는거지 근데 연산자의 개수가 계속 달라지니까 for문의 개수도 달라지잖아
그럼 for문이 아니라 재귀함수를 사용해야하네! 그럼 무엇을 의미하는 재귀함수를 만들어야 할까? 또 재귀함수의 매개변수와 리턴값은? 
현재 k개의 연산자를 골랐고 k+1개의 수를 계산했으며 k+1번 째 연산자를 고르고 k+2번째 수와 결과를 연산하는 메서드
매개변수에 k들어가야하고 연산의 결과 result도 들어가야하겠네
해당 메서드를 사용했는지 사용하지 않았는지 체크하는 checked 리스트도 필요할거고 
근데 checked 리스트의 구성은?? 일단 연산자가 4개인건 확정인데 개수가 매 케이스마다 달라질 수 있잖아 2차원 리스트를 활용해야 할까? 그거보단 개수 리스트에서 -1을 해주는게 나을거같은데
그러면 어떻게 모든 조합을 고려하지?? 체크리스트로 하나씩 체크하는건 알겠는데 한바퀴 돌았을 때 어떻게 체크리스트의 처음으로 돌아가냐는거임 
while문으로 뺑뻉이 돌려?"""
# N 입력 받기
N = int(input())

# N개의 숫자 입력 받기
numbers = list(map(int,input().split()))

# 4종류, N-1개의 연산자 개수 받기 + - * / 순으로
operations = list(map(int,input().split()))

# maxResult, mimResult 선언 및 초기화
maxResult = int(-1e9)
minResult = int(1e9)

# 현재 k번째 연산자를 뽑을 차례이고 result와 index k 숫자를 연산하는 메서드
def backtracking(k, result, plus, minus, multiply, divide):
    global maxResult, minResult
    
    # base condition, backtracking
    if k == N:
        if maxResult < result:
            maxResult = result
        if minResult > result:
            minResult = result
        return
    
    # k != N
    if plus:
        backtracking(k+1, result + numbers[k], plus-1, minus, multiply, divide)
    if minus:
        backtracking(k+1, result - numbers[k], plus, minus-1, multiply, divide)
    if multiply:
        backtracking(k+1, result * numbers[k], plus, minus, multiply-1, divide)
    if divide:
        backtracking(k+1, int(result / numbers[k]), plus, minus, multiply, divide-1)

# 메서드 실행
backtracking(1, numbers[0], operations[0], operations[1], operations[2], operations[3])

# 결과 출력
print(maxResult)
print(minResult)


