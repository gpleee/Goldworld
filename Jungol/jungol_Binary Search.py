def solution(N,ai,Q,bi):

    answer = []
    low = 0
    high = N-1

    for i in range(Q):

        while low <= high:
            
            mid = (low + high) // 2

            if ai[mid] == bi[i]:
                answer.insert(i,ai[mid])
            
            elif ai[mid] > bi[i]:
                high = mid - 1

            else:
                low = mid + 1
        
        if not ai[i]:
            answer.insert(i,-1)

    return answer

print(solution(5,[1,2,3,4,5],3,[-5,5,2]))