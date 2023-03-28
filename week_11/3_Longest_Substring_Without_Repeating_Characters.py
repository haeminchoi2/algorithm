# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        
        if not s:
            return 0
        
        if len(s) == 1:
            return 1
        
        else:
            for i in range(1, len(s) + 1):
                for j in range(len(s)):
                    if len(s[j:j+i]) == i and len(s[j:j+i]) == len(set(s[j:j+i])):
                        print(s[j:j+i])
                        print(s.count(s[j:j+i]))
                        answer = max(answer, len(s[j:j+i]))
            print(answer)
            return answer

s = Solution()
s.lengthOfLongestSubstring(s = "au")