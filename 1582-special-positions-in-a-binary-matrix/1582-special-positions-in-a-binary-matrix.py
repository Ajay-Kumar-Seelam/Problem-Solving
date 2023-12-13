class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        count = 0
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                j = mat[i].index(1)
                x = list(zip(*mat))
                if sum(x[j]) == 1:
                    count += 1
        return count