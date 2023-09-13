class BSTIterator:
    def __init__(self, root):
        # Initialize an empty stack for iterative in-order traversal.
        self.stack = []
        # Initialize the pointer to the smallest node.
        self.pointer = root

    def hasNext(self):
        # The iterator has next if there are items in the stack or if the pointer is not None.
        return self.stack or self.pointer

    def next(self):
        # Perform in-order traversal to get the next smallest element.
        while self.pointer:
            self.stack.append(self.pointer)
            self.pointer = self.pointer.left
        
        # Pop the top element from the stack.
        node = self.stack.pop()
        # Move the pointer to the right child of the popped element.
        self.pointer = node.right
        
        # Return the value of the popped element.
        return node.val