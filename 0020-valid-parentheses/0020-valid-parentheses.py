class Solution:
    def isValid(self, s: str) -> bool:
       stack = []
       bracket_map = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the string
       for char in s:
        if char in bracket_map:  # If it's a closing bracket
            # Pop the top of the stack if it's not empty, otherwise use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the popped element matches the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:  # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # If the stack is empty, it means all brackets were matched
       return not stack