# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        array = nums1 + nums2
        print(array)
        array.sort()
        print(array)
        
        if len(array) % 2 == 0:
            return (array[len(array)//2] + array[len(array)//2 - 1]) / 2
        else:
            return array[len(array)//2]

a = Solution()
a.findMedianSortedArrays(nums1 = [1,3], nums2 = [2])