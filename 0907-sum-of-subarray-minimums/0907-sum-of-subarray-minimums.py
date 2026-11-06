class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        n=len(arr)
        mod=10**9+7
        left=[0]*n
        right=[0]*n
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                left[i]=i-stack[-1]
            else:
                left[i]=i+1
            stack.append(i)
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and arr[stack[-1]]>arr[i]:
                stack.pop()
            if stack:
                right[i]=stack[-1]-i
            else:
                right[i]=n-i
            stack.append(i)
        ans=0
        for i in range(n):
            contribution=arr[i]*left[i]*right[i]
            ans=(ans+contribution)%mod
        return ans
        