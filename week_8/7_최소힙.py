# https://www.acmicpc.net/problem/1927

import heapq
import sys


# n = 9
n = int(sys.stdin.readline())

x = [int(sys.stdin.readline()) for _ in range(n)]
# x = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]

array = []

heapq.heapify(array)

for item in x:
    if item == 0 and array:
        data = heapq.heappop(array)
        print(data)
    elif item == 0 and not array:
        print(0)
    
    else:
        heapq.heappush(array, item)


