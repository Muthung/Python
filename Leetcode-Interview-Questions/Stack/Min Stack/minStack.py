class MinStack:
    def __init__(self):
        self.stack = []  # Actual stack to store elements
        self.min_stack = []  # Stack to keep track of minimum elements

    def push(self, val: int) -> None:  # <-- Add the colon (:) after 'val int'
        self.stack.append(val)

        # If the min_stack is empty or the new element is less than or equal to the current minimum, update the min_stack
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the element from the stack
        val = self.stack.pop()

        # If the popped element is the current minimum, also remove it from the min_stack
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the minimum element from the min_stack (the top of the min_stack contains the minimum element)
        return self.min_stack[-1]