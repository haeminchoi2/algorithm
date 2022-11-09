# https://school.programmers.co.kr/learn/courses/30/lessons/42862


def solution(n, lost, reserve):
    answer = 0

    for lost_student in lost:
        if lost_student in reserve:
            reserve.remove(lost_student)
            lost.remove(lost_student)
    
    for reserve_student in reserve:
        if reserve_student - 1 in lost:
            lost.remove(reserve_student - 1)
        
        elif reserve_student + 1 in lost:
            lost.remove(reserve_student + 1)
    print(lost)
    answer = n - len(lost)

    return answer

print(solution(5, [2, 4], [3]))
# 