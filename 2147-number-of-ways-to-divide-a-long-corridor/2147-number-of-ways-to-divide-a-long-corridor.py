class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        index = []
        n = 0 
        
        for (i, char) in enumerate(corridor):
            if char == "S":
                n += 1 
                index.append(i)
                
        if n == 0 or n % 2 == 1: 
            return 0 
        
        ans = 1
        
        for i in range(1, n - 1, 2):
            ans *= (index[i + 1] - index[i])
            
        return ans % MOD