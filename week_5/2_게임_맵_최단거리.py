# https://school.programmers.co.kr/learn/courses/30/lessons/1844

m = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]


############################################## DFS 구현 실패
# def dfs(maps, node, cnt):
#     global answer
    
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, -1, 1]

#     if node[0] == len(maps[0])-1 and node[1] == len(maps)-1: # x좌표와 y좌표가 목적지에 도착
#         answer = cnt
        
#     for i in range(len(dx)):
#         to_x = node[0] + dx[i]
#         to_y = node[1] + dy[i]
#         if len(maps[0]) > to_x >= 0 and len(maps) > to_y >= 0 and maps[to_y][to_x] == 1:
#             maps[node[1]][node[0]] = 0 # 이미 방문한 노드 벽으로 간주
#             dfs(maps, (to_x, to_y), cnt+1)


# def solution(maps):
#     global answer
#     answer = len(maps) * len(maps[0])
#     dfs(maps, (0, 0), 1)
    
#     if answer == len(maps) * len(maps[0]):
#         return -1
#     return answer

from collections import deque


def bfs(maps, node):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque()
    queue.append(node)
    # visited = []
    
    while queue:
        x, y = queue.popleft()
        
        if [x, y] == [len(maps)-1, len(maps[0])-1]: # 목표 지점에 도달했다면
            return maps[x][y]
        
        for i in range(len(dx)):
            to_x = x + dx[i]
            to_y = y + dy[i]
            
            if 0 <= to_x < len(maps) and 0 <= to_y < len(maps[0]) and maps[to_x][to_y] == 1:
                # if [x, y] not in visited:
                    # queue.append([to_x, to_y])
                    # visited.append([x, y])
                maps[to_x][to_y] = maps[x][y] + 1
                queue.append([to_x, to_y])
    # return len(visited)
    return -1 # while문이 끝나는 동안 함수가 종료되지 않았다면, 도달 하지 못한것으로 간주 -> -1 반환

# def solution(maps):
    # return bfs(maps, [0, 0])
print(bfs(m, [0, 0]))
