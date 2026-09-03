class Solution:
    def maxPower(self, s: str) -> int:
        count=1
        maxi=1
        for i in range(1,len(s)):
            if s[i-1]==s[i]:
                count=count+1
            else:
                count=1
            maxi=max(maxi,count)
        return maxi
        
        