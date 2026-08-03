class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        """ Time complexity is o(n) because we are visiting all characters
            Space complexity is o(n) because strings are immutable in python so we are converting all the characters and storing the all characters"""
            
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            
            left=left+1
            right=right-1
       
            

        