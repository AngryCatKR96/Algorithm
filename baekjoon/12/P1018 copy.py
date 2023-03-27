"""브루트 포스 -> 모든 경우의 수, 2초 시간 넉넉함, 
일단 전체 배열을 리스트로 받음 왼쪽위부터 8x8 배열 추출, 추출한 8x8배열에서 몇개 칠해야하는지 카운트
다시 칠해야하는 정사각형의 개수 어떻게 구하지?
색이 번갈아가며 나와야하는데 무작정 다음 색과 다르다고 카운트를 해주면 안된다 BBB면 하나만 바꾸면되는데 두개씩 비교하면 두번카운트 되기때문
그러면 세개씩 비교하면? BBBBBBBBWBWBW 근데 처음 값을 기준으로 해도되나? 뒤에 두개 바꿔야한다고 해도 조삼모사일듯?
"""
N, M = map(int, input().split())

board = []
for i in range(N):
    board.append(list(input()))
    
black = ['B','W','B','W','B','W','B','W']
white = ['W','B','W','B','W','B','W','B']    
minList = []
for i in range(0, N-7): # 행 실행 횟수
    for j in range(0, M-7): # 열 실행 횟수
        subBoard = []
        count = 0
        countB = 0
        countW = 0
        for k in range(0,8): # 2차원 subBoard 만들기
            subBoard.append(board[i+k][j:j+8])
        # subBoard 체크
        for row in range(0,8):
                if row%2 == 0 : # 짝수 인덱스
                    for col in range(0,8):
                        if subBoard[row][col] != black[col]:
                            countB += 1
                else:
                    for col in range(0,8):
                        if subBoard[row][col] != white[col]:
                            countB += 1

                if row%2 == 0 : # 짝수 인덱스
                    for col in range(0,8):
                        if subBoard[row][col] != white[col]:
                            countW += 1
                else:
                    for col in range(0,8):
                        if subBoard[row][col] != black[col]:
                            countW += 1
        if countB < countW: 
            count=countB
        else: 
            count = countW
        minList.append(count)                    
        
print(min(minList))