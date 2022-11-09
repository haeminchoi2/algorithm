# https://school.programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    str_n = str(n)
    for number in str_n:
        answer += int(number)
    return answer