class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        n=len(s)
        while i <n and s[i]==' ':
            i=i+1
        if i==n:
            return 0
        sign=1
        if s[i]=='-':
            sign=-1
            i=i+1
        elif s[i]=='+':
            i+=1
        num=0
        while i <n and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        num=sign*num
        INT_MAX=2**31-1
        INT_MIN=-2**31
        if num>INT_MAX:
            return INT_MAX
        if num<INT_MIN:
            return INT_MIN
        return num
        