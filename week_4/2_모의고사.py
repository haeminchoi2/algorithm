# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    
    for index, answer in enumerate(answers):
        if answer == person1[index % len(person1)]:
            cnt[0] += 1
        if answer == person2[index % len(person2)]:
            cnt[1] += 1
        if answer == person3[index % len(person3)]:
            cnt[2] += 1
    
    answer = []
    if cnt.count(max(cnt)) == 3:
        answer = [1, 2, 3]
        return answer
    
    elif cnt.count(max(cnt)) > 1:
        for index, score in enumerate(cnt):
            if max(cnt) == score:
                answer.append(index + 1)
                cnt.pop(index)
    else:
        answer.append(cnt.index(max(cnt)) + 1)
    
    return answer

print(solution([1,3,2,4,2]))