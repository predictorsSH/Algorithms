#leetcode 4 : Meduan of Two Sorted Arrays
#https://leetcode.com/problems/median-of-two-sorted-arrays


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = sorted(nums1+nums2)
        if len(result) % 2 != 0:
            return result[len(result)//2]
        else :
            return (result[len(result)//2-1]+result[(len(result)//2)])/2