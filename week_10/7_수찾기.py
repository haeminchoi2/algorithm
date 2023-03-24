# https://www.acmicpc.net/problem/1920

import bisect

# n = 5
n = int(input())

# a = [4, 1, 5, 2, 3]
a = list(map(int, input().split()))
a.sort()

# print(a)
x = int(input())
m = list(map(int, input().split()))
# print(m)
# m = [1, 3, 7, 9, 5]


for num in m:
    i = bisect.bisect_left(a, num)
    if i < len(a) and num == a[i]:
        print(1)
    else:
        print(0)


