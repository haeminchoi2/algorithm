# https://www.acmicpc.net/problem/1015

n = int(input())
a = list(map(int, input().split()))
array = sorted(a)
answer = []
for i in a:
    answer.append(str(array.index(i)))
    array[array.index(i)] = 0

print(" ".join(answer))