# https://leetcode.com/problems/longest-palindromic-substring/

#################################################
# 내 풀이
# class Solution:
#     def is_pal(self, n):
#         for i in range(len(n)//2):
#             if n[i] != n[len(n) - i - 1]:
#                 return False
#         return True
    
#     def longestPalindrome(self, s: str) -> str:
#         sub = s[:]
#         l, r = 0, len(s)
#         while True:
#             if l == r:
#                 return s[l - 1]
            
#             if self.is_pal(sub):
#                 print(sub)
#                 return sub
#             else:
#                 l += 1
#                 r -= 1
#             sub = s[l:r]
        

##########################################
# 1. easy ver.
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         for i in range(len(s), 0, -1):
#             for j in range(len(s)-i+1):
#                 sub = s[j:j+i]
#                 if sub == sub[::-1]:
#                     return sub
#         return ''

###############################################
# 2. two pointer
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ''

        for i in range(len(s) - 1):
            result = max(result,
                        expand(i, i + 1),
                        expand(i, i + 2),
                        key=len)

        return result
a = Solution()
a.longestPalindrome(s='abb')