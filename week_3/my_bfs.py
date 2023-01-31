graph = dict()
 
graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

from collections import deque


def bfs(graph, root, visited):
    queue = deque([root])
    visited = []
    
    while queue:
        visit = queue.popleft()
        if visit not in visited:
            queue.extend(graph[visit])
            visited.append(visit)
    return visited

print(bfs(graph, 'A', []))