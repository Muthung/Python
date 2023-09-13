## Binary Search Tree Iterator

### Question

Implement the *BSTIterator* class that represents an iterator over the **in-order traversal** of a binary search tree (BST):

*BSTIterator(TreeNode root)* Initializes an object of the *BSTIterator* class. The *root* of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.

*boolean hasNext()* Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.

*int next()* Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to *next()* will return the smallest element in the BST.

You may assume that *next()* calls will always be valid. That is, there will be at least a next number in the in-order traversal when *next()* is called.

#### Implementation

The *BSTIterator* class takes the root of the BST as input during initialization.

Teh *hasNext* method checks whether there are more elements to traverse. It returns *True* if there are elements in the stack(yet to be visited) or if the pointer is not *None*.

The *next* method performs an in-order traversal. It uses a stack to keep track of nodes to visit and a pointe to traverse the tree. It pushes nodes onto the stack as it goes left and returns the values as it pops them off the stack.