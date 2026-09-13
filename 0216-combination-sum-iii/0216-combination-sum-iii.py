class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        def solve(start,current,total):
            if len(current)==k:
                if total==n:
                    result.append(current.copy())
                return
            if total>n:
                return
            for i in range(start,10):
                current.append(i)
                solve(i+1,current,total+i)
                current.pop()
        solve(1,[],0)
        return result
        