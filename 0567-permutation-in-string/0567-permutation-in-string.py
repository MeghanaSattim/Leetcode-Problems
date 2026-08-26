from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = Counter(s1)
        n = len(s1)

        for i in range(len(s2) - n + 1):
            window = s2[i:i+n]

            if Counter(window) == target:
                return True

        return False
      
       
    
        