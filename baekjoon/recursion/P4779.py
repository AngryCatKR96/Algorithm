while True:
    try:
        # N 입력받기
        N = int(input())
        
        n = pow(3,N)
        
        # 칸토어 메서드 정의
        def cantor(n):
            # base conditon : 길이가 1이면 리턴
            if n == 1:
                return '-'
            str = cantor(n//3)
            return str + ' '*(n//3) + str
        
        # 메서드 실행
        print(cantor(n))
        
    except:
        break



    