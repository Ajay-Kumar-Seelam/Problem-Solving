class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d , res = defaultdict(list) , []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d[i+j].append(nums[i][j])
        for k in d.values():
            k = k[::-1]
            res.extend(k)
        return res