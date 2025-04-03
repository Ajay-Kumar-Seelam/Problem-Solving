class Solution {
    public long maximumTripletValue(int[] nums) {
        int n =nums.length;
        long[] prefix = new long[n];
        long[] suffix = new long[n];
        prefixMax(prefix,nums);
        suffixMax(suffix,nums);
        long ans = 0;
        for(int j=1;j<n-1;j++)
        {
            ans = Math.max(ans,(prefix[j-1] - nums[j])*suffix[j+1]);
        }
        return ans;

    }
    private void prefixMax(long[] prefix,int[] nums)
    {
        long max = prefix[0] = nums[0];
        for(int i=1;i<nums.length;i++)
        {
            max = Math.max(max,nums[i]);
            prefix[i] = max;
        }
    }
    private void suffixMax(long[] suffix,int[] nums)
    {
        long max = suffix[nums.length-1] = nums[nums.length-1];
        for(int i=nums.length-2;i>=0;i--)
        {
            max = Math.max(max,nums[i]);
            suffix[i] = max;
        }
    }
}