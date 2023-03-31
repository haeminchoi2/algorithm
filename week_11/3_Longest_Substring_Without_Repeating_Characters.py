# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        q = deque()
        visited = {}
        
        for i in s: # 문자열을 하나씩 돌면서
            if i in visited: # 방문했던 문자인지 확인하고 같은 문자라면 이전 문자을 계속 지워줄 것이다.
                pop_item = None # pop한 아이템을 저장하기 위한 초기화
                while pop_item != i: # pop한 아이템이 현재 원소와 같을 때까지
                    pop_item = q.popleft()
                    if pop_item in visited:
                        visited.pop(pop_item)
            q.append(i) # if문 안거쳤다면, q에 넣어서 substring을 만들어간다
            visited[i] = i
            
            answer = max(answer, len(q))
        print(answer)
        return answer


s = Solution()
s.lengthOfLongestSubstring(s = "abcabcbb")

#############################

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         answer = 0
        
#         if not s:
#             return 0
        
#         if len(s) == 1:
#             return 1
        
#         else:
#             for i in range(1, len(s) + 1):
#                 for j in range(len(s)):
#                     if len(s[j:j+i]) == i and len(s[j:j+i]) == len(set(s[j:j+i])):
#                         print(s[j:j+i])
#                         print(s.count(s[j:j+i]))
#                         answer = max(answer, len(s[j:j+i]))
#             print(answer)
#             return answer
