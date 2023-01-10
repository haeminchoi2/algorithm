from itertools import combinations

def is_prime_number(number):
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def solution(nums):
    combin_list = list(combinations(nums, 3))
    answer = 0
    
    for combin in combin_list:
        if is_prime_number(sum(combin)):
            answer += 1
    return answer


print(solution([1,2,3,4]))