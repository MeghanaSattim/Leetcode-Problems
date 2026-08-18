class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for nums in seen:
            if nums-1 not in seen:
                currentSum=nums
                count=1
                while currentSum+1 in seen:
                  currentSum=currentSum+1
                  count=count+1
                longest=max(longest,count)
        return longest
        
           

                
        
    
                
           
        