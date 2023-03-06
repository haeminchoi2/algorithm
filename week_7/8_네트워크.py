# https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    answer = list()
    
    for i in range(n):
        q = deque(list())
        q.append(i)
        visited = []
        
        while q:
            visit = q.popleft()
            if visit not in visited:
                for j in range(len(computers[visit])):
                    if computers[visit][j] == 1 and j != visit:
                        q.append(j)
            visited.append(visit)
        
        if set(visited) not in answer:
            answer.append(set(visited))
        
    return len(answer)

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
