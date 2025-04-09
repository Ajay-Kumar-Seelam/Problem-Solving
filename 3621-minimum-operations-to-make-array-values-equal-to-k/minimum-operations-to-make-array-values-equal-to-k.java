class Solution {
    public int minOperations(int[] nums, int k) {
        int mini = Integer.MAX_VALUE;
        for (int num : nums) mini = Math.min(mini, num);
        if (mini < k) return -1;

        HashSet<Integer> st = new HashSet<>();
        for (int num : nums) st.add(num);
        return st.size() - (mini == k ? 1 : 0);
    }
}