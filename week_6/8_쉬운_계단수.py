# https://www.acmicpc.net/problem/10844

n = 2

dp = [[0 for _ in range(10)] for _ in range(n)]
# dp_ = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#       [1, 1, 2, 2, 2, 2, 2, 2, 2, 1],
#       [1, 3, 3, 4, 4, 4, 4, 4, 3, 2]]

dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
            
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
            
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[n-1])%1000000000)

###
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# /10, 11, /12, 13, 14, 15, 16, 17, 18, 19
# 20, /21, 22, /23, 24, 25, 26, 27, 28, 29
# 30, 31, /32, 33, /34, 35, 36, 37, 38, 39
# ...
# 100, /101, 102, 103, 104, 105, 106, 107, 108, 109
# 110, 111, 112, 113, 114, 115, 116, 117, 118, 119
# 120, /121, 122, /123, 124, 125, 126, 127, 128, 129
# ...

## n=2일때
# 1의 자리가 
# 0일 때
# 앞에는 1
# 1일 때
# 2
# 2일 때
# 1, 3
# ...
# 8일 때
# 7, 9
# 9일 때
# 8

### n=3

# 1의 자리가 0일 때
# 10의자리 = 1
# 100의자리 = 2

# 1일 때
# 10의자리 = 0, 2
# 100의 자리 = 0: 1
# 2: 1, 3

# 2일 때
# 10의 자리 = 1, 3
# 100의 자리 = 1: 2
# 3: 2, 4

# 3일 때
# 10의 자리 = 2, 4
# 100의 자리 = 2: 3, 1
# 4: 3, 5
# i = 2
# dp[2][2] = dp[1][1] + dp[1][3]

# 4일 때
# 10의 자리 = 3, 5
# 100의 자리 = 3: 2, 4
# 5: 4, 6
# ...
# 8일 때
# 10의 자리 = 7, 9
# 100의 자리 = 7: 6, 8
# 9: 8

# 9일 때
# 10의 자리 = 8
# 100의 자리 = 8: 7, 9

#### n = 4

# 1의자리 0
# 10의 자리 1
# 100의 자리 0, 2
# 1000의 자리 0: 1
# 2: 1, 3