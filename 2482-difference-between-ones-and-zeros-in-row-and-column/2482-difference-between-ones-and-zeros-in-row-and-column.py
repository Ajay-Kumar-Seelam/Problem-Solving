class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        numRow = len(grid)
        numCol = len(grid[0])
        matrix = [[0 for y in range(numCol)] for x in range(numRow)]  
        mapRow = [0] * numRow
        mapCol = [0] * numCol

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                mapRow[i] += grid[i][j]
                mapCol[j] += grid[i][j]

        for i in range(0, numRow):
            for j in range(0, numCol):
                matrix[i][j] = 2 * mapRow[i] + 2 * mapCol[j] - numRow - numCol

        return matrix