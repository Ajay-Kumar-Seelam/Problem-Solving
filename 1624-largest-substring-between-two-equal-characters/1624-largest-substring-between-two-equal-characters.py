class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans=-1
        for i in range(0,len(s)):
            j=len(s)-1
            
            c=s[i]
            while j>=0 and i<j:
                if s[j]==c:
                    ans=max(ans,j-i-1)
                j-=1
        return ans
                
        