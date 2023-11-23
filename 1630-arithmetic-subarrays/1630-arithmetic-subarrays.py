class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        def check(tmp):
            diff = tmp[1] - tmp[0]
            for i in range(len(tmp)-1):
                if tmp[i+1] - tmp[i] != diff : return False 
            return True 
        
        
        ans = [] 
        
        for i in range(len(l)):
            tmp = sorted(nums[l[i]:r[i]+1])
            ans.append(check(tmp))
            
        return ans 