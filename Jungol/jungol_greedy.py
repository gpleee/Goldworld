def sol(a,b,c,d,e,N):
    answer = 0

    #16그램 추
    while N>=16 and e>=1:
        e -= 1
        N -= 16
        answer += 1
    
    #8그램 추
    while N>=8 and d>=1:
        d -= 1
        N -= 8
        answer += 1

    #4그램 추    
    while N>=4 and c>=1:
        c -= 1
        N -= 4
        answer += 1

    #2그램 추
    while N>=2 and b>=1:
        b -= 1
        N -= 2
        answer += 1

    #1그램 추
    while N>=1 and b>=1:
        b -= 1
        N -= 1
        answer += 1
    
    if N != 0:
        answer = "impossible"

    return answer

print(sol(10,10,10,0,10,))