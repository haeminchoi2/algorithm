# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# cnt = 0

# def dfs(numbers, target, index, sum, length):
#     global cnt
    
#     if index == length:
#         if sum == target:
#             cnt += 1
#         return
#     dfs(numbers[index:], target, index + 1, sum + numbers[index], length)
#     dfs(numbers[index:], target, index + 1, sum - numbers[index], length)
    
# dfs([1, 1, 1, 1, 1], 3, 0, 0, 5)

# def solution(numbers, target):
#     return dfs(numbers, target, 0)


####################################
def dfs(numbers, target, sum):
    if len(numbers) == 0:
        if sum == target:
            return 1
        else:
            return 0
    return dfs(numbers[1:], target, sum + numbers[0]) + dfs(numbers[1:], target, sum - numbers[0])

def solution(numbers, target):
    return dfs(numbers, target, 0)

print(solution([1, 1, 1, 1, 1], 3))