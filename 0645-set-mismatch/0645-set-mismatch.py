class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic=set()
        ans=[]
        n=len(nums)
        for i in nums:
            if i not in dic:
                dic.add(i)
            else:
                ans.append(i)
        for i in range(1,n+1):
            if i not in dic:
                ans.append(i)
        return ans
                
                
                
                
                
        