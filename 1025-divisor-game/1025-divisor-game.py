class Solution:
    def divisorGame(self, n: int) -> bool:
        memo = [-1] * (n+1)  # Initialize memoization array

        def fun(n: int):
            if n == 1:
                return False
            if memo[n] != -1:
                return memo[n]

            for i in range(1, n):
                if n % i == 0 and not fun(n - i):
                    memo[n] = True
                    return True

            memo[n] = False
            return False

        return fun(n)
