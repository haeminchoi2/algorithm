# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    array = list(map(str, numbers))
    array.sort(key=lambda x: (x * 3), reverse=True)
    
    return str(int("".join(array)))

solution([0, 0, 0])



