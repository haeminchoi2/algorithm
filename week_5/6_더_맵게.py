# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        result = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, result)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K: # pop하고 push가 반복되어 모든 음식을 섞었을 때와 그 스코빌 지수가 K보다 작을때
            return -1
    
    return answer