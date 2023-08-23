## Same Tree

### Question

Given the roots of two binary trees *p* and *q*, write a fuction to check if they are the same or not.

Two binary trees are considered the same if they are structually identical, and the nodes have the same value.

#### Implementation

The *isSameTree* function takes two parameters: *p* and *q,* which are the roots of the two binary trees being compared.

The base cases of the recursion are handled first:

If both *p* and *q* are *None*, it means we've reached the end of both trees, and they are identical. So, we return *True*.
    
If either *p* or *q* is *None* while the other is not, the trees are not identical in structure, so we return *False*.

If the base cases are not met, we check if the values of the current nodes *p.val* and *q.val* are equal. If they are not equal, the trees cannot be identical, so we return *False*.

If the values are equal, we need to check the left and right subtrees of both trees. We do this by recursively calling the *isSameTree* function for the left subtrees *(p.left and q.left)* and the right subtrees *(p.right and q.right)*.

The result of the recursive calls for both subtrees is combined using the logical *and* operator. If both subtrees are structurally identical and have the same node values, the overall result will be *True*; otherwise, it will be *False.*

Finally, the combined result is returned from the function.