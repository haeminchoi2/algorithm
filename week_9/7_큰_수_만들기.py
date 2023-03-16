# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = []
    cnt = 0
    
    for i in range(len(number)):
        if i == 0:
            answer.append(number[i])
            continue
        
        # 이전에 넣은 숫자들이 현재 숫자보다 작으면 다 지워주기 위함
        while answer and int(answer[-1]) < int(number[i]) and cnt != k:
            if int(answer[-1]) < int(number[i]):
                answer.pop()
                cnt += 1
        answer.append(number[i])
        
    if cnt < k:
        answer = answer[:-(k - cnt)]
    
    return "".join(answer)

solution("7777777", 2)