class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        
        for i in range(0,k):
            minv=nums[0]
            mini=0
            
            for j in range(1,len(nums)):
                if minv>nums[j]:
                    
                    mini=j
                    minv=nums[j]
            nums[mini]=multiplier*minv
        return nums
        