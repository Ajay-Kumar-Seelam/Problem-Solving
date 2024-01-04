class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        ans=0
        for v in freq.values():
            if v==1:
                return -1
            if v %3==0:
                ans+=v//3
                
            elif v%3==2:
                v=v-2
                ans+=1
                ans+=v//3
            elif v%3==1:
                v=v-1
                ans+=1
                ans+=v//3
                
                
            else:
                ans+=v//2
                
        return ans
        