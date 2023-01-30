# https://school.programmers.co.kr/learn/courses/30/lessons/86971

g = {1: [3], 2: [3], 3: [1, 2], 4: [5, 6, 7], 5: [4], 6: [4], 7: [4, 8, 9], 8: [7], 9: [7]}

cnt = 0

def dfs(node, graph, visited):
    global cnt
    visited.append(node)
    cnt += 1
    for near in graph[node]:
        if not near in visited:
            dfs(near, graph, visited)


def solution(n, wires):
    global cnt
    answer = n
    
    # 간선 자르기
    for index, wire in enumerate(wires):
        copy_wires = wires[:]
        cut = copy_wires.pop(index)
        
        # 자른 후 그래프 만들기
        graph = {i : [] for i in range(1, n+1)}
        for wire in copy_wires:
            node1, node2 = wire
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # 노드 갯수 체크하기
        check = []
        for num in range(1, n+1):
            cnt = 0
            dfs(num, graph, [])
            check.append(cnt)
        answer = min(answer, abs(max(check) - min(check)))
        
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))