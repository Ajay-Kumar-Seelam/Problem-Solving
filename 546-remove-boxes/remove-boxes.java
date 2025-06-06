class Solution {
    public int removeBoxes(int[] boxes) {
        int n = boxes.length;
        int[][][] dp = new int[n][n][n];

        return helper(boxes, 0, n - 1, 0, dp);
    }

    private int helper(int[] boxes, int i, int j, int k, int[][][] dp) {
        if (i > j) return 0;

        if (dp[i][j][k] != 0) return dp[i][j][k];

        int origI = i, origK = k;

        // Optimization: merge contiguous same-colored boxes
        while (i + 1 <= j && boxes[i] == boxes[i + 1]) {
            i++;
            k++;
        }

        // Remove [i...i+k]
        int max = (k + 1) * (k + 1) + helper(boxes, i + 1, j, 0, dp);

        // Try to merge later same-colored boxes
        for (int m = i + 1; m <= j; m++) {
            if (boxes[m] == boxes[i]) {
                max = Math.max(max, helper(boxes, i + 1, m - 1, 0, dp) + helper(boxes, m, j, k + 1, dp));
            }
        }

        dp[origI][j][origK] = max;
        return max;
    }
}
