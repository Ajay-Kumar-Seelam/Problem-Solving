class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        
        prefix=[1]*len(nums)
        temp=[]
        for i in nums:
            temp.append(i%2)
            
        for i in range(1,len(nums)):
            if temp[i]!=temp[i-1]:
                prefix[i]=prefix[i]+prefix[i-1]
                
        print(prefix)
        ans=[]
        for [i,j] in queries:
            if j-i==prefix[j]-prefix[i]:
                ans.append(True)
            else:
                ans.append(False)
            
        return ans
        