"""세 개의 점에서 점 하나만 추가해서 축에 평행한 직사각형이 된다는 말은 처음 세개의 점들이 축에 평행한 직각 삼각형을 이루고 있다는 뜻이다
직사각형이면 같은 x좌표 두개 같은 y좌표 두개가 나와야 하므로 부족한 애들을 각각 좌표에 넣어준다"""

# 좌표 입력
xList = []
yList = []
for i in range(3):
    x, y = map(int,input().split())
    xList.append(x)
    yList.append(y)
    
# x, y 각각 좌표 개수 세서 하나밖에 없으면 그게 답임
resultX = 0
resultY = 0
for i in range(3):
    if xList.count(xList[i]) == 1:
        resultX = xList[i]
    if yList.count(yList[i]) == 1:
        resultY = yList[i]
        
print(resultX, resultY)