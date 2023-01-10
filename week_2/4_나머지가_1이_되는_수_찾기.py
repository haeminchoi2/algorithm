def solution(n):
    answer = 0
    for number in range(2, n):
        if n % number == 1:
            return number