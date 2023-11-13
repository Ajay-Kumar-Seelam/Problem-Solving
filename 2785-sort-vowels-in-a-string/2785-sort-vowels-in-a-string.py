class Solution:
    def sortVowels(self, s: str) -> str:
        ans=""
        ans1=[i for i in s if i not in "aeiouAEIOU"]
        ans2=sorted([ i for i in s if i in "aeiouAEIOU"])

        for i in s:
            if i in ans1:
                ans+=i

            else:
                ans+=ans2.pop(0)

        return ans 
