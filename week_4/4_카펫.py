# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    n = (brown - 4) // 2
    for i in range(n):
        if i * (n - i) == yellow:
            answer = [i + 2, n - i + 2] # 위아래, 양옆으로 한칸씩 brown을 붙혀 늘어나기 때문
    return answer