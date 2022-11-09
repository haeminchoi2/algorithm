# https://school.programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    for i in str(n)[::-1]:
        answer.append(int(i))
    return answer