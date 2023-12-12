class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first=max(nums[0],nums[1])
        second=min(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            if nums[i]>= first:
                second=first
                first=nums[i]
            elif nums[i]>second and nums[i]<=first:
                second=nums[i]
        return (first-1)*(second-1)
                
        