# https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    answer = new_id
    answer = answer.lower() # 1단계
    
    answer = "".join(re.findall(r"[a-z0-9-_.]", answer)) # 2단계
    
    answer = re.sub(r"[.]+", ".", answer) # 3단계
    
    answer = answer.strip(".") # 4단계
    
    if answer == "": # 5단계
        answer = "a"
    
    if len(answer) > 15: # 6단계
        answer = answer[:15].strip(".") # 아이디 규칙에 처음과 끝에는 마침표를 사용할 수 없음.
    
    if len(answer) <= 2: # 7단계
        while len(answer) < 3:
            answer += answer[-1]
    
    return answer
