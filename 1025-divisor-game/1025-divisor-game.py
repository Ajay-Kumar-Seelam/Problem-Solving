class Solution:
    def divisorGame(self, n: int) -> bool:
        # Dictionary for memoization
        memo = {}

        def fun(n: int, t: int):
            # Check if the result is already computed
            if n in memo:
                return memo[n]

            if n < 1:
                return False
            elif n == 1 and t % 2 == 0:
                return True
            elif n == 1 and t % 2 != 0:
                return False
            
            for i in range(1, n):
                if i == 1:
                    result = fun(n - 1, t + 1)
                elif i > 1 and n % i == 0:
                    fact1 = i
                    fact2 = n // i
                    result = fun(n - fact1, t + 1) or fun(n - fact2, t + 1)
                
                memo[n] = result  # Store the result in the memo dictionary
                if result:
                    return True

            return False

        return fun(n, 1)
