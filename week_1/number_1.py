# https://school.programmers.co.kr/learn/courses/30/lessons/12944?language=python3
arr_ = [1, 2, 3, 4, -12]

def solution(arr):
    answer = sum(arr) / len(arr)
    return answer
print(solution(arr_))