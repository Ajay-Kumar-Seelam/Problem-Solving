class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        for i in range(len(prices)-1):
            x=prices[i]+prices[i+1]
            if x == money:
                return 0
            elif x < money:
                return money-x
        return money