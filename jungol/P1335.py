import sys

# 2차원 리스트를 잘라서 새로 만든다는 생각을 하지말고 기존에 있는 리스트를 인덱스를 활용해서 탐색한다고 생각하자


def color(inputList, row, col, n): # n은 가로길이 row, col는 각각 시작 지점
    global white
    global blue
    if n == 1:
        if inputList[row][col] == '1':
            blue += 1
        else:
            white += 1
        return
    
    firstColor = inputList[row][col]
    for i in range(row, row+n):
        for j in range(col, col+n):
            if inputList[i][j] != firstColor: # 색이 다를때만
                # 네등분하기
                color(inputList, row, col, int(n/2) )# 왼쪽위
                color(inputList, row, col+int(n/2), int(n/2) )# 오른쪽위
                color(inputList, row+int(n/2), col, int(n/2) )# 왼쪽아래
                color(inputList, row+int(n/2), col+int(n/2), int(n/2) )# 오른쪽아래
                return
      
    #  전부 같은 색이면 카운트 증가            
    if firstColor == '1':
        blue += 1
    else:
        white += 1  
                
        

# 입력
N = int(sys.stdin.readline())

colorList = []
for i in range(N):
    colorList.append(list(sys.stdin.readline().strip().split()))

# 변수 초기화
white = 0
blue = 0
        
# 메서드 실행
color(colorList, 0, 0, N)

# 카운트 출력
print(white)
print(blue)
