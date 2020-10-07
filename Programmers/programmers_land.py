def sol(land):
    answer = 0
    com = 0

    for i in land:

        maxval = land[i][0]
        
        for j in range(4):

            if j != com:
                if maxval < land[i][j]:
                    maxval = land[i][j]
                    com = j

        answer += maxval
    
    return answer