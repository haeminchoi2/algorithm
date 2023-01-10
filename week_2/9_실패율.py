def solution(N, stages):
    fails = [[i+1, 0] for i in range(N)]
    
    for index in range(len(fails)):
        fails[index][1] = stages.count(index + 1) / len(list(lambda x: x for stage in stages if stage >= index + 1))
    
    fails.sort(key= lambda x:x[1], reverse=True)
    
    answer = [fail[0] for fail in fails]
    
    return answer

print(solution(4, [4,4,4,4,4]))