class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(curr,opencount,closecount):
            if len(curr)==2*n:
                result.append(curr)
                return
            if opencount<n:
                backtrack(curr+"(",opencount+1,closecount)
            if closecount<opencount:
                backtrack(curr+")",opencount,closecount+1)
        backtrack("",0,0)
        return result