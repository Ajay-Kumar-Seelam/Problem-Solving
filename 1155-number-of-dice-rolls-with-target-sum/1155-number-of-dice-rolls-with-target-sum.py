class Solution:
    def numRollsToTargetu(self, d, f, target,memo):
        if d==0 and target==0:
            return 1
        elif d==0 or target<0:
            return 0
        elif (d,target) in memo:
            return memo[(d,target)]
        else:
            ans = 0
            for i in range(1,f+1):
                ans+=self.numRollsToTargetu(d-1,f,target-i,memo)
            memo[(d,target)] = ans%((10**9)+7)
            return memo[(d,target)]
        
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        return self.numRollsToTargetu(d,f,target,memo)