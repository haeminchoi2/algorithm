# https://school.programmers.co.kr/learn/courses/30/lessons/86491

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

def solution(sizes):
    w = 0
    h = 0
    
    for size in sizes:
        if w < max(size):
            w = max(size)
        if h < min(size):
            h = min(size)
    return w * h

print(solution(sizes))