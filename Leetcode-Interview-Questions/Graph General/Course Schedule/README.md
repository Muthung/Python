## Course Schedule

### Question

There are a total of *numCoures* courses ou have to take, labeled from *0* to *numCourses - 1*. You are given an array *prerequisites* where *prerequisites[i} = [ai, bi]* ndicates that you **must** take course *bi* first if you want to take course *ai*.

    -  For example, the pair *[0, 1]*, indicates that to take course *0* you have to take course *ai*.

Return *true* if you can finish all courses. Otherwise, return *false*.

#### Implementation

First, create a graph representation where each course is a node, and prerequisites are directed edges between nodes.

Implement a depth-first search (DFS) function *'is_cyclic'* to detect cycles in the graph. If a cycle is found, it meand you cannot finish all courses.

Initialize a list *'visited'* to keep track of the visited nodes during DFS. Use values -1 for nodes in the current traversal, 1 for nodes that are visited and not part of a cycle, and 0 for unvisited nodes.

Iterate through all courses and checks for cycles by callig *'is_cyclic'* for each course. If any course is part of a cycle, return *'False'*. Otherwise, return *'True'* at the end.

