# https://www.acmicpc.net/problem/11279

import heapq
import sys


# n = 13
n = int(sys.stdin.readline())

x = [int(sys.stdin.readline()) for _ in range(n)]
# x = [0, 1, 2, 0, 0, 3, 2, 1, 0, 0, 0, 0, 0]

array = []

heapq.heapify(array)

for item in x:
    if item == 0 and array:
        data = heapq.heappop(array)
        print(-data)
    elif item == 0 and not array:
        print(0)
    
    else:
        heapq.heappush(array, -item)