import java.util.*;

class Solution {
    public int largestIsland(int[][] grid) {
        int N = grid.length;
        Map<Integer, Integer> sizeMap = new HashMap<>(); // Island label -> size
        int label = 2;
        
        // 1. Precompute areas
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (grid[r][c] == 1) {
                    sizeMap.put(label, dfs(grid, r, c, label));
                    label++;
                }
            }
        }
        
        // 2. Try flipping water
        int res = sizeMap.isEmpty() ? 0 : Collections.max(sizeMap.values());
        
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (grid[r][c] == 0) {
                    res = Math.max(res, connect(grid, r, c, sizeMap));
                }
            }
        }
        
        return res;
    }
    
    private int dfs(int[][] grid, int r, int c, int label) {
        int N = grid.length;
        if (r < 0 || c < 0 || r >= N || c >= N || grid[r][c] != 1) {
            return 0;
        }
        
        grid[r][c] = label;
        int size = 1;
        
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        for (int[] dir : directions) {
            size += dfs(grid, r + dir[0], c + dir[1], label);
        }
        
        return size;
    }
    
    private int connect(int[][] grid, int r, int c, Map<Integer, Integer> sizeMap) {
        int N = grid.length;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        Set<Integer> visitedLabels = new HashSet<>();
        int size = 1;
        
        for (int[] dir : directions) {
            int nr = r + dir[0], nc = c + dir[1];
            if (nr >= 0 && nc >= 0 && nr < N && nc < N && grid[nr][nc] > 1) {
                int islandLabel = grid[nr][nc];
                if (!visitedLabels.contains(islandLabel)) {
                    size += sizeMap.get(islandLabel);
                    visitedLabels.add(islandLabel);
                }
            }
        }
        
        return size;
    }
}
