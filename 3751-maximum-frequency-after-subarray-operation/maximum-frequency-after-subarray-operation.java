class Solution {
    public int maxFrequency(int[] nums, int k) {
        Map<Integer,Integer> freqmap=new HashMap();
        
        int maxfreq=0;
        freqmap.put(k,0);
        for (int i=0;i<nums.length;i++){
            if(!freqmap.containsKey(nums[i])){
                freqmap.put(nums[i],1);
            }
        else{
            freqmap.put(nums[i],freqmap.get(nums[i])+1);
        }
                }

        for (Integer val:freqmap.keySet()){
            maxfreq=Math.max(maxfreq,calculate(nums,val,k));

        }
            
        
    return freqmap.get(k)+maxfreq;
    }

    private int calculate(int[] nums,int value,int k){
        int maxGain=0,currentGain=0;

        for(int num:nums){
            if(num==k) currentGain--;
            if (num==value) currentGain++;
            if (currentGain<0) currentGain=0;
            maxGain=Math.max(maxGain,currentGain);
        }
    return maxGain;

    }
}