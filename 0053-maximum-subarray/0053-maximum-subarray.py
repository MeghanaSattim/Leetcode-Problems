class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=nums[0]
        maximum=nums[0]
        for i in range(1,len(nums)):
            current=max(nums[i],nums[i]+current)
            maximum=max(current,maximum)
        return maximum
        