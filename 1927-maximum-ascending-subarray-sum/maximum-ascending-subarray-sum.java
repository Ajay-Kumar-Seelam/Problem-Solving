class Solution {
    public int maxAscendingSum(int[] nums) {
        int ans=nums[0],curr=nums[0];

        for(int i=1;i<nums.length;i++){
            
            if(nums[i]>nums[i-1])
            curr+=nums[i];

            else{
                curr=nums[i];
            }
            ans=Math.max(ans,curr);
        }
        
    return ans;}
}