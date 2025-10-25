class Solution:
    def triSum(self, n: int) -> int:
        return (n * (n + 1)) >> 1

    def totalMoney(self, days: int) -> int:
        nWeeks, rDays = divmod(days, 7)        
        return self.triSum(days) - 42 * self.triSum(nWeeks - 1) - 6 * nWeeks * rDays
