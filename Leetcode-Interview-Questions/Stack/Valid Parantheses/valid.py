def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:  # If char is a closing bracket
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:  # If char is an opening bracket
            stack.append(char)
    
    return not stack  # If stack is empty, all brackets were matched