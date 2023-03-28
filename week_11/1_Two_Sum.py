# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                if num1 + num2 == target:
                    return [i, j]

a = Solution()
a.twoSum(nums = [2,7,11,15], target = 9)