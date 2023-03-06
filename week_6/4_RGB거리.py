# https://www.acmicpc.net/problem/1149

n = 3
# n = int(input())

arr = [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
# arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    arr[i][0] = min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0]
    arr[i][1] = min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1]
    arr[i][2] = min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2]

print(min(arr[n-1]))

##########
# RGB
# i = 1
# 
# dp = [0] * (n+1)

# for i in range(1, n):
#     dp[i] = min(min(arr[i - 1][1], arr[i - 1][2]) + arr[i][0], 
#                 min(arr[i - 1][0], arr[i - 1][2]) + arr[i][1], 
#                 min(arr[i - 1][0], arr[i - 1][1]) + arr[i][2])

# print(dp)
###########

