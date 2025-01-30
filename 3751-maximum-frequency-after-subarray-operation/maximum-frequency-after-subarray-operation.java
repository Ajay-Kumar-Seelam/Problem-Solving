class Solution {
    public int maxFrequency(int[] nums, int k) {
        
        Map<Integer,Integer> count=new HashMap();
        count.put(k,0);
        int ans=0;
        for(int num:nums){
            if(!count.containsKey(num)){
                count.put(num,1);
            }
            else
            {
                count.put(num,count.get(num)+1);
            }
        }
        for(int n:count.keySet()){
            ans=Math.max(ans,calculate(nums,n,k));
            //System.out.println(n+" "+k);
        }
        System.out.println(ans);
    return count.get(k)+ans;
    }
    public int calculate(int[] nums, int value,int k){
        int maxGain=0,curr=0;
        for (int i=0;i<nums.length;i++){
            if(nums[i]==k) curr=Math.max(0,curr-1);

            else if(nums[i]==value) curr++;
            maxGain=Math.max(maxGain,curr);
        }
        return maxGain;

    }
    
}