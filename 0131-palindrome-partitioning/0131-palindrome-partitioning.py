class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def isPalindrome(string):
            return string==string[::-1]
        def solve(index,current):
            if index==len(s):
                result.append(current.copy())
                return
            for end in range(index,len(s)):
                substring=s[index:end+1]
                if isPalindrome(substring):
                    current.append(substring)
                    solve(end+1,current)
                    current.pop()
        solve(0,[])
        return result
        