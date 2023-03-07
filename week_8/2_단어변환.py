# https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque


def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visited = [False for _ in range(len(words))]
    
    while q:
        text, cnt = q.popleft()
        if text == target:
            return cnt
        
        for i in range(len(words)):
            diff_alpha = 0
            if not visited[i]: # words 안에 있는 단어를 현재 방문 안했을때 실행
                for j in range(len(text)):
                    if text[j] != words[i][j]: # 텍스트 알파벳 순서와 단어의 알파벳과 다를때
                        diff_alpha += 1
                if diff_alpha == 1: # 다른 알파벳이 1개일때만 변환할 수 있다.
                    q.append([words[i], cnt + 1])
                    visited[i] = True
    
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


##################################
# def solution(begin, target, words):
#     answer = 0
#     begin_list = [text for text in begin]
#     target_list= [text for text in target]
#     for word in words:
#         cnt = 0
#         for i in range(len(word)):
#             if word[i] != begin[i] and word[i] in target_list:
#                 cnt += 1
#         if cnt == 1:
#             begin = word
#             answer += 1
#             print(begin)
#     print(answer)
    
#     print(target_list)
#     return answer

