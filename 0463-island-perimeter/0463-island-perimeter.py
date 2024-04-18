class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # # of rows and cols
        nrows, ncols = len(grid), len(grid[0])
        seen = [[False for c in range(ncols)] for r in range(nrows)]  # tiles we've seen
    
        def dfs(r: int, c: int):
            # if out of bounds or water
            if (r < 0) or (r == nrows) or (c < 0) or (c == ncols) or not grid[r][c]:
                return 1
            # if we've seen this land before
            if seen[r][c]:
                return 0
            # new land, update seen
            else:
                seen[r][c] = True
            # run again on all surrounding tiles
            return dfs((r - 1), c) + dfs(r, (c - 1)) + dfs((r + 1), c) + dfs(r, (c + 1))
    
        # find land
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]:
                    return dfs(i, j)