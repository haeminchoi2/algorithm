# https://www.acmicpc.net/problem/2579
# n = int(input())
# array = list(int(input()) for _ in range(n))
n = 2

array = [10, 20]

dp = [0] * n

if n == 1:
    print(array[0])

elif n == 2:
    print(array[0] + array[1])

else:
    dp[0] = array[0]
    dp[1] = array[0] + array[1]
    dp[2] = max(array[1] + array[2], array[0] + array[2])

    for i in range(3, n):
        dp[i] = max(dp[i-3] + array[i-1] + array[i], dp[i-2] + array[i])

    print(dp[n-1])
##################
# 1, 2, 4, 6
# i = 1

# dp[0] + array[1] # i-1, i
# dp[0] + array[2] # i-1, i+1
###################

################
# 마지막 계단을 꼭 밟밟
# == 현재 계단을 기준으로 이전에 밟았는지 아닌지

# index = 3
# 0, 1, 3 => dp[1] + array[3]
# 1, 3 array[1] + array[3]

# index = 4
# 0, 1, 3, 4 
#     => dp[3] + array[4]
#     => dp[1] + array[3] + array[4]
#     => dp[4-3] + array[3] + array[4]

# 0, 2, 3
#     => dp[2] + array[4-1]
#     =====>>>>> 4번 인덱스가 마지막이라면 꼭 밟아야하므로 따져야할 필요 없음
# 0, 2, 4
#     => dp[2] + array[4]
#     => dp[4-2] + array[4]
# 1, 2, 4
#     => dp[2] + array[4]
#     => dp[4-2] + array[4]

# index = 5
# 0, 1, 3, 4 => x
# 0, 1, 3, 5 => dp[5-2] + array[5]
# 0, 2, 3, 5 => dp[2] + array[3] + array[5]
# => dp[5-3] + array[3] + array[5]
# 1, 2, 4, 5 => dp[4-2] + array[4] + array[5]
# 1, 2, 4 -> x
# 1, 3, 4 -> x
#######################



