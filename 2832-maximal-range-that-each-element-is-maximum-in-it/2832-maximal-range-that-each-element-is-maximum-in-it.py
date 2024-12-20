from sortedcontainers import SortedList

class Solution:
    def maximumLengthOfRanges(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ins = SortedList()
        
        for i in sorted(range(len(nums)), key=lambda i: nums[i], reverse=True):
            j = ins.bisect_left(i)
            l = 0 if j == 0 else ins[j-1] + 1
            r = len(nums) if j == len(ins) else ins[j]
            ans[i] = r - l
            ins.add(i)
            
        return ans