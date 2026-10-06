class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack=[]

        for asteriod in asteroids:
            alive =True
            while stack and stack[-1]>0 and asteriod <0:
                if stack[-1] <-asteriod:
                    stack.pop()
                elif stack[-1]==-asteriod:
                    stack.pop()
                    alive=False
                    break
                else:
                    alive=False
                    break
            if alive:
                stack.append(asteriod)
        return stack
        