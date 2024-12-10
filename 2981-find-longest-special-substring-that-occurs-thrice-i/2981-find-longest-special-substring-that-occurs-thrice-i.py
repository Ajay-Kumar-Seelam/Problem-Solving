class Solution:
    def maximumLength(self, s: str) -> int:
        book = defaultdict(int)
        ans = -1
        for l in range(1, len(s)+1):
            for i in range(len(s)+1-l):
                
                if s[i:i+l] == s[i] * l:
                    book[s[i:i+l]] += 1
                if book[s[i:i+l]] >= 3:
                    ans = max(ans, l)
        return ans