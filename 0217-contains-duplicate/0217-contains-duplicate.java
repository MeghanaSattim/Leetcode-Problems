class Solution {
    public boolean containsDuplicate(int[] nums) {
        HashMap<Integer,Integer>map=new HashMap<>();
        for(int freq:nums)
        {
            map.put(freq,map.getOrDefault(freq,0)+1);
        }
        
        for(int count:map.values())
        {
            if(count>1)
            {
                
                return true;
                
            }
        }
        return false;
    }
}