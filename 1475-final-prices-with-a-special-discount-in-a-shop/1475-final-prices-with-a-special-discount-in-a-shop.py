class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        
        for i in range(0,len(prices)):
            j=i+1
            while j<len(prices):
                if prices[i]>=prices[j]:
                    ans.append(prices[i]-prices[j])
                    j=len(prices)
                else:
                    j+=1
            if len(ans)==i:
                ans.append(prices[i])
        return ans
                
                    
                
        