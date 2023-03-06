# https://www.acmicpc.net/problem/1932

# n = int(input())
# array = []
# for i in range(n):
#     array.append(list(map(int, input().split())))

n = 5
array = [     [7], 
             [3, 8], 
           [8, 1, 0], 
          [2, 7, 4, 4], 
         [4, 5, 2, 6, 5]]
dp = []
dp.append([array[0][0]])
# dp.append([dp[0][0] + array[1][0], dp[0][0] + array[1][1]])

# dp[2] = [dp[1][0] + array[2][0], 
#           dp[1][0] + array[2][1], 
#           dp[1][0] + array[2][2] ...]
# dp = [([0] * n) for _ in range(n)]
# dp[0][0] = array[0][0]

if n == 1:
    print(array[0][0])

else:
    for i in range(1, n):
        temp = []
        for j in range(i + 1):
            if j == 0:
                temp.append(dp[i - 1][j] + array[i][j])
            elif j == i:
                temp.append(dp[i - 1][j - 1] + array[i][j])
            else:
                temp.append(max(dp[i - 1][j - 1] + array[i][j], dp[i - 1][j] + array[i][j]))
                # temp.append(dp[i - 1][j] + array[i][j])
        dp.append(temp)
        print(dp)
    print(max(dp[n-1]))