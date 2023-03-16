# https://www.acmicpc.net/problem/2606

n = int(input())
x = int(input())

graph = {}
for i in range(1, n + 1):
    graph[i] = []

for j in range(x):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)


# 1       4
# 2 5     7
# 3 6
# graph = {1: [2, 5],
#          2: [1, 3, 5],
#          3: [2],
#          4: [7],
#          5: [1, 2, 6],
#          6: [5],
#          7: [4]}


def dfs(n, v):
    v.append(n)
    for near in graph[n]:
        if not near in v:
            v = dfs(near, v)
    return v

print(len(dfs(1, [])) - 1)
