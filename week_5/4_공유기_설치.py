# https://www.acmicpc.net/problem/2110

import bisect

# n, c = map(int, input().split())
n, c = 5, 3

list_ = [1, 2, 8, 4, 9]
# list_ = []
# for _ in range(n):
#     list_.append(int(input()))

list_.sort()
print(list_)
start = list_[0]
end = list_[-1]

while start <= end:
    mid = bisect.bisect_left(list_, (start+end) // 2)
    print("mid", mid)
    distance = list_[mid] - start
    # print(distance)
    if start == end:
        print(start - list_[0])
        break
    
    count = (list_[-1] - list_[0]) / distance
    if count == c:
        print(distance)
        break
    if count < c:
        end = list_[mid - 1]
    else:
        start = list_[mid + 1]

