# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    grade = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    cnt = 0
    for num in lottos:
        if num in win_nums:
            cnt += 1
    
    answer.append(grade[cnt + lottos.count(0)])
    answer.append(grade[cnt])
    
    return answer

solution([31, 10, 45, 1, 6, 19], [31, 10, 45, 1, 6, 19])