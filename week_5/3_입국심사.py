# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    
    start = 1 # 최소 시간은 1분
    end = times[-1] * n # 최대 시간
    
    while start <= end:
        mid = (start + end) // 2
        people = 0 # mid 시간동안 심사할 수 있는 사람 수
        for time in times:
            people += mid // time
        
        if people < n:
            start = mid + 1
        else: # answer를 계속 갱신하며, while문 끝날때 까지 반복
            end = mid - 1
            answer = mid
            
    return answer

