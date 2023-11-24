class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles)
        n=len(piles)-2
        c=0
        b=len(piles)//3
        for i in range(b):
            c+=piles[n]
            n-=2
        return c