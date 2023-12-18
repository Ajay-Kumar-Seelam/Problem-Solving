class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)*max1
        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)*min1
        return max2-min2