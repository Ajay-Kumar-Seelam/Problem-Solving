class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        bucket = Counter(chars)
        ans = 0

        for word in words:
            c = Counter(word)
            flag = True
            for char, count in c.items():
                if char not in bucket or bucket[char]< c[char]:
                    flag = False
                    break
            if flag:
                ans += len(word)

        return ans
