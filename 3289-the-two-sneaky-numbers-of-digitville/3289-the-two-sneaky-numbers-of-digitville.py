class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        temp=[]
        ans=[]
        for i in nums:
            if i not in temp:
                temp.append(i)
            else:
                ans.append(i)
        return ans
                
        