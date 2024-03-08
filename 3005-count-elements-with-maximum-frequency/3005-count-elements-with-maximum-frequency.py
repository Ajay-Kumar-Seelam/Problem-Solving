class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        freq={}
        maxs,ans=0,0
        for i in nums:
            curr=0
            if i not in freq:
                freq[i]=1
                curr=1
            else :
                temp=freq[i]
                freq[i]=temp+1
                curr=temp+1
            if curr>maxs:
                maxs=curr
                
        for key in freq:
            if freq[key]==maxs:
                ans=ans+maxs
        return ans
    