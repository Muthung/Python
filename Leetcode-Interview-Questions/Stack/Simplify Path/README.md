## Simplify Path

### Question

Given a string *path*, which is an **absolute path** (starting with a slash *'/'*) to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period *'.'* refers to the current directory, a double period *'..'* refers to the directory up a level, and any multiple consecutive slashes (i.e. *'//'*) are treated as a single slash *'/'*. 

For this problem, any other format of periods such as *'...'* are treated as file/directory names.

The canonical path should have the following format:

    The path starts with a single slash *'/'*.

    Any two directories are separated by a single slash *'/'*.

    The path does not end with a trailing *'/'*.

    The path only contains the directories on the path from the root directory to the target file or directory (i.e., no period *'.'* or double period *'..'*)

Return the simplified canonical path.

#### Implementation

Split the input path by slashes to obtain individual components (directories and file names).

Initialize an empty stack to keep track of the canonical path.

Iterate through each component obtained from step 1.

For each component, handle the following cases:

    a. If it is a single period ('.'), simply skip it as it refers to the current directory.

    b. If it is a double period ('..'), pop the top element from the stack (if the stack is not empty) as it refers to going up one level.

    c. If it is an empty string or contains only slashes, skip it as it represents consecutive slashes.

    d. For any other valid component, push it onto the stack.

After processing all components, construct the simplified canonical path using the elements in the stack.