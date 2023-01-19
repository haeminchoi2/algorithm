# https://school.programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations

def is_prime_number(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers_list = list(numbers)
    perm = []
    
    for i in range(1, len(numbers_list)+1):
        perm += list(permutations(numbers_list, i))
    
    all_number = [int("".join(num)) for num in perm]
    
    for num in all_number:
        if is_prime_number(num):
            answer.append(num)
    return len(set(answer))

print(is_prime_number(1))
print(solution("011"))