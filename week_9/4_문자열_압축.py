# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = len(s) + 1
    for i in range(1, len(s)//2 + 2): # 가장 크게 잘랐을 때가 절반이므로
        string = ""
        cnt = 1
        slicing = s[:i] # 먼저 쪼개본다
        
        for j in range(i, len(s) + i, i):
            if slicing == s[j:j+i]: # ex) 2abc라면 2를 카운트하기 위해
                cnt += 1
            else:
                if cnt == 1: # 일치하는게 없다면, 쪼개본것을 string에 추가해준다.
                    string += slicing
                else: # string에 2abc처럼 추가해준다.
                    string += str(cnt) + slicing
                slicing = s[j:j+i]
                cnt = 1
        
        answer = min(answer, len(string))
    return answer

solution('aabbaccc')