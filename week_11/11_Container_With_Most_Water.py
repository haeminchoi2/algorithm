# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list) -> int:
        if len(height) == 2:
            return min(height[0], height[1])
        left = 0
        right = len(height) - 1
        water = 0
        while left <= right:
            a = right - left
            b = min(height[left], height[right])
            if water < a * b:
                water = a * b
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water

h = [1,8,6,2,5,4,8,3,7]

x = Solution()
x.maxArea(height= h)