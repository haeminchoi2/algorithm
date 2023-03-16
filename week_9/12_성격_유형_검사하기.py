# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = [1, 1, 1, 1]
    types = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    array = {}
    for t in types:
        array[t[0]] = 0
        array[t[1]] = 0
    
    for type, choice in zip(survey, choices):
        if choice < 4: # 비동의 선택
            array[type[0]] += abs(choice - 4)
        if choice > 4: # 동의 선택
            array[type[1]] += abs(choice - 4)
        else:
            continue
    
    for i, v in enumerate(types):
        left, right = v
        if array[left] > array[right]:
            answer[i] = left
        elif array[left] < array[right]:
            answer[i] = right
        else:
            answer[i] = sorted(v)[0]
    
    return "".join(answer)

solution(["TR", "RT", "TR"], [7, 1, 3])