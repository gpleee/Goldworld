R, C, T = map(int,input().split())
A = [[0]*C]

#1행부터 R행 입력받기
for i in range (1,R+1): 
    A.append([0]+list(map(int,input().split())))

#공기청정기 위치
count = 1
for i in range (1,R+1):
        if A[i][1] == -1:
            AChigh = i
            break
AClow = AChigh +1


for t in range(T):

    #(퍼뜨려진 먼지)만 B1에 저장
    B1 = [[0]*(C+1)]*(R+1)
    for i in range(1,R+1):
        for j in range(1,C+1):
            if A[i][j]//5 > 0:
                if i+1 < R+1:
                    B1[i+1][j] += A[i][j]//5
                if j+1 < C+1:
                    B1[i][j+1] += A[i][j]//5
                if i-1 > 0:
                    B1[i-1][j] += A[i][j]//5
                if j-1 > 0:
                    B1[i][j-1] += A[i][j]//5
        print(B1)    

    #(기존먼지 - 빠져나간 먼지)를 B2에 저장
    B2 = [[0]*(C+1)]*(R+1)
    for i in range(1,R+1):
        for j in range(1,C+1):
            check = 0
            if A[i][j]//5 > 0:
                if i+1 < R+1:
                    check +=1
                if j+1 < C+1:
                    check +=1
                if i-1 > 0:
                    check +=1
                if j-1 > 0:
                    check +=1
            B2[i][j] = A[i][j] - (A[i][j]//5)*check 
    
    #B = B1 + B2
    B = [[0]*(C+1)]*(R+1)
    for i in range(1,R+1):
        for j in range(1,C+1):
            B[i][j] = B1[i][j] + B2[i][j]