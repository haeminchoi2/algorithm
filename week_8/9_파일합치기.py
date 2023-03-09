# https://www.acmicpc.net/problem/11066

k = 4
files = [40, 30, 30, 50]

dp = []

dp.append(files[0])
dp.append(files[0] + files[1])
dp.append(min(dp[1] + files[2], dp[0] + files[2] + files[1]))

if k == 3:
    print(sum(dp[1:]))

for i in range(3, len(files)):
    # dp.append(min(dp[i - 2] + files[i] + files[i - 1], dp[1] + files[i]))
    dp.append(min(files[0] + files[1] + files[2] + files[3],
                  files[1] + files[2] + files[0] + files[1] + files[2]))

print(dp)

