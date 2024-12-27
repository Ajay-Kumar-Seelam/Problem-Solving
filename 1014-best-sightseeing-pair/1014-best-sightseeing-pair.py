class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        ans=0
#         for i in range(0,len(values)):
#             for j in range(i+1,len(values)):
                
#                 ans=max(ans,values[i]+values[j]+i-j)
        cur_max=values[0]-1
        for i in range(1,len(values)):
            ans=max(ans,values[i]+cur_max)
            cur_max=max(cur_max-1,values[i]-1)
            
        
        return ans
                
                
        
        
        
        