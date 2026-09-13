class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        def solve(index,current,total):
            if total==target:
                result.append(current.copy())
                return 
            
            if index==len(candidates) or total>target:
                return
            current.append(candidates[index])
            solve(index,current,total+candidates[index])
            current.pop()
            solve(index+1,current,total)
        solve(0,[],0)
        return result