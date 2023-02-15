# https://www.acmicpc.net/problem/2156

# n = int(input())
n = 6


# glass = [int(input()) for _ in range(n)]
# glass = [0]
# for i in range(n):
    # glass.append(int(input()))
glass = [0, 6, 10, 13, 9, 8, 1]

drink = [0]

############ 경우의 수
# 3번째 잔을 마실 때
# 1, 2 못마시거나 ===> drink[3-1]
# 1, 3 이전의 잔을 안먹거나 ===> drink[3-2] + 현재와인
# 2, 3 이전 이전의 잔을 안먹거나 ===> 이전와인 + 현재와인

# 4번째 잔을 마실 때
# 1, 2, 4 마시거나
# 4-3, 4-2, 4
# ===> drink[4-2] + 현재와인

# 1, 3, 4 마시거나
# n만 생각했을때, 4-3, 4-1, 4
# ===> drink[4-3] + 이전와인 + 현재와인

# 2, 3 못마시거나
# 4-2, 4-1
# ===> drink[4-1]

# 5번째 잔을 마실 때
# 1, 2, 4, 5 마시거나
# 1, 3, 4 못마시거나
# 2, 3, 5 마시거나
############

drink.append(glass[1])

if n > 1:
    drink.append(glass[1] + glass[2])

for i in range(3, n+1):
    drink.append(max(drink[i-1], drink[i-2] + glass[i], drink[i-3] + glass[i-1] + glass[i]))
                    #못마시거나      이전의 잔을 안마셨을 때             이전 이전의 잔을 안마셨을 때
print(drink[n])
