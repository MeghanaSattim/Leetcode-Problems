class Solution {
    public int[] applyOperations(int[] nums) {
        int n=nums.length;
        int k=0;
        for(int i=0;i<n-1;i++)
        {
            if (nums[i]==nums[i+1])
            {
                nums[i]=nums[i]*2;
                nums[i+1]=0;
            }
        }
        for(int i=0;i<n;i++)
        {
            if(nums[i]!=0)
            {
              nums[k]=nums[i];
              k=k+1;
            }
        }
        while (k<n)
        {
            nums[k]=0;
            k=k+1;
        }
        return nums;
        
    }
}