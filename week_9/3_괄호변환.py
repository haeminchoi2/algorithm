# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def div(p):
    l = 0
    r = 0
    for i in range(len(p)):
        if p[i] == "(":
            l += 1
        elif p[i] == ")":
            r += 1
        
        if l == r:
            return p[:i+1], p[i+1:] # u, v

def check(u):
    array = []
    
    for i in u:
        if i == "(":
            array.append(i)
        else:
            if not array:
                return False
            array.pop()
    return True

def solution(p):
    answer = ''
    
    if not p: # 1단계
        return ''
    
    u, v = div(p) # 2단계
    
    if check(u): # 3단계
        return u + solution(v)
    
    else: # 4단계
        answer += "("
        answer += solution(v)
        answer += ")"
        for item in u[1:len(u) - 1]:
            if item == "(":
                answer += ")"
            else:
                answer += "("
    
    return answer

solution("(()())()")