# 그래프 표현 (예시)
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

# 재귀를 이용한 DFS
# def dfs(node, visited = []):
#     visited.append(node)
#     for near in graph[node]:
#         if not near in visited:
#             visited = dfs(near, visited)
#     return visited

# 스택을 이용한 DFS
def my_dfs(graph, node):
    visited = []
    stack = [node]
    
    while stack:
        visit = stack.pop()
        if visit not in visited:
            visited.append(visit)
            stack.extend(graph[visit])
    return visited

print(my_dfs(graph, 'A'))