class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMin=nums[0]
        currentMax=nums[0]
        result=nums[0]
        for i in range(1,len(nums)):
            num=nums[i]
            if num<0:
                currentMin,currentMax=currentMax,currentMin
            currentMax=max(num,num*currentMax)
            currentMin=min(num,num*currentMin)
            result=max(currentMax,result)
        return result
        