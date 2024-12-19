class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_max=-1
        ans=0
        
        
        for i,n in enumerate(arr):
            cur_max=max(n,cur_max)
            
            if cur_max==i:
                ans+=1
        
                
            
        return ans
            
            
        