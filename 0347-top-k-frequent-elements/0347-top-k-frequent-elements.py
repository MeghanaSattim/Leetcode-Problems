class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        items=list(freq.items())
        items.sort(key=lambda x:x[1],reverse=True)
        return [items[i][0] for i in range(k)]
        