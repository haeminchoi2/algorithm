import heapq


def solution(jobs):
    answer = 0
    time = 0
    cnt = 0
    h = []
    start = -1
    
    while len(jobs) > cnt:
        for job in jobs:
            if start < job[0] <= time: # 작업이 진행되는 사이에 대기할 수 있는 작업을 걸러내는 분기문
                heapq.heappush(h, [job[1], job[0]])

        if len(h) > 0:
            data = heapq.heappop(h)
            start = time
            time += data[0]
            answer += (time - data[1]) # 대기하면서 작업종료까지의 시간
            cnt += 1
        else: # 힙에 작업이 없는 경우 +1초
            time += 1
        
    return int(answer / len(jobs))

solution([[0, 3], [1, 9], [2, 6]])
