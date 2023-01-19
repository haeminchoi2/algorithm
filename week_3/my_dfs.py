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

####################
def dfs(node, visited = []):
    visited.append(node)
    for near in graph[node]:
        if not near in visited:
            visited = dfs(near, visited)
    return visited

#####################
# def my_dfs()
print(dfs('A'))