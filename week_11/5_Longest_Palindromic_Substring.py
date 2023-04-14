# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def is_pal(self, n):
        for i in range(len(n)//2):
            if n[i] != n[len(n) - i - 1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        sub = s[:]
        l, r = 0, len(s)
        while True:
            if l == r:
                return s[l - 1]
            
            if self.is_pal(sub):
                return sub
            else:
                l += 1
                r -= 1
                sub = s[l:r]
            
    
a = Solution()
a.longestPalindrome(s='ac')