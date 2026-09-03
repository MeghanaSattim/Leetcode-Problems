class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=0
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[k]=nums[i]
                k=k+1
        while k<n:
            nums[k]=0
            k=k+1
        return nums
        