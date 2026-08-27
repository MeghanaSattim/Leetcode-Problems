class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        mini=float('inf')
        
        for right in range(len(nums)):
            sum=sum+nums[right]
            while sum>=target:
                mini=min(mini,right-left+1)
                sum=sum-nums[left]
                left=left+1
            
        if mini==float('inf'):
            return 0
        return mini
                


            

        