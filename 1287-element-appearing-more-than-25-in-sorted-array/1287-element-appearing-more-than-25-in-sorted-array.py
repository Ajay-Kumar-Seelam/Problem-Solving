class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n=len(arr)
        dis={}
        n=n/4
        
        for i in arr:
            if i not in dis:
                dis[i]=1
            else:
                dis[i]=dis[i]+1
            if dis[i]>n:
                return i
            
        