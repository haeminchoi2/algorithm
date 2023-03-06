# https://www.acmicpc.net/problem/11053

n = 6
arr = [10, 20, 10, 30, 20, 50]

dp = [0] * n
# [1, 2, 1, 3, 2, 4]
#####
# 10 = 1
# 20 = 10보다 크니까 2
# 10 = 20보다 작아서 1
# 30 = 20보다 크니까 3
# 20 = 
# 50 = 30보다 크니까 4

#####

for i in range(n): # 현재 숫자를 비교하기
    for j in range(i): # 현재 숫자까지의 수를 비교하기
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))