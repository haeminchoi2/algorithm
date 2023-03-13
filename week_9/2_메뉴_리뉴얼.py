# https://school.programmers.co.kr/learn/courses/30/lessons/72411


def solution(orders, course):
    answer = []
    array = {}
    orders = sorted(orders, key=lambda x: len(x))
    for order in orders:
        alpha_set = {alpha for alpha in order}
        
        for diff in orders:
            diff_set = {x for x in diff}
            inner = alpha_set & diff_set
            key = "".join(sorted(inner))
            if key and len(key) in course:
                array[key] = 0
    
    for key in array:
        for order in orders:
            if set(key) & set(order) == set(key):
                array[key] += 1
    
    maximum = list(map(lambda x: [x, y] for y in array, course))
    print(maximum)
    return array

solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,4])