def solution(d, budget):
    d.sort()
    cnt = 0
    
    ###################### case1
    for money in d:
        if budget >= money:
            budget -= money
            cnt += 1
        else:
            break
    return cnt
    
    ####################### case2
    # while 

print(solution([2,2,3,3], 10))