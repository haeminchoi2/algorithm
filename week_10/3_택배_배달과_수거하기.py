# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def deli(box, cap, n, deliveries):
    if sum(deliveries) > cap:
        for i in range(n, 0, -1):
            if box + deliveries[i - 1] <= cap:
                box += deliveries[i - 1]
                deliveries[i - 1] = 0
            else:
                deliveries[i - 1] -= cap - box
                box += cap - box
            
            if box == cap:
                return deliveries
    else:
        deliveries = [0 for _ in range(n)]
        return deliveries

def pick(box, cap, n, pickups):
    if sum(pickups) > cap:
        for i in range(n, 0, -1):
            if box + pickups[i - 1] <= cap:
                box += pickups[i - 1]
                pickups[i - 1] = 0
            else:
                pickups[i - 1] -= cap - box
                box += cap - box
            
            if box == cap:
                return pickups
    else:
        pickups = [0 for _ in range(n)]
        return pickups

def solution(cap, n, deliveries, pickups):
    answer = 0
    for num in range(n, 0, -1):
        if deliveries[num - 1] == 0 and pickups[num - 1] == 0:
            continue
        deliveries = deli(0, cap, num, deliveries)
        pickups = pick(0, cap, num, pickups)
        answer += num * 2
        print(deliveries)
        print(pickups)
        print(answer)
    return answer

# cap = 2
n = 7
deliveries = [1, 0, 2, 0, 1, 0, 2]
pickups = [0, 2, 0, 1, 0, 2, 0]

solution(cap, n, deliveries, pickups)
