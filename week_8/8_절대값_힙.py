# https://www.acmicpc.net/problem/11286

import heapq


n = 18
x = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]

array = []

heapq.heapify(array)

for item in x:
    if item == 0 and array:
        data = heapq.heappop(array)
        print(data[1])
    elif item == 0 and not array:
        print(0)
    
    else:
        heapq.heappush(array, [abs(item), item])
        