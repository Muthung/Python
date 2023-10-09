## Course Schedule II

### Question

There are a total of *numCoures* courses ou have to take, labeled from *0* to *numCourses - 1*. You are given an array *prerequisites* where *prerequisites[i} = [ai, bi]* ndicates that you **must** take course *bi* first if you want to take course *ai*.

    -  For example, the pair *[0, 1]*, indicates that to take course *0* you have to take course *1*.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

#### Implementation

This solves the problem of course scheduling by utilizing Kahn's algorithm for topological sorting.

It constructs a directed graph where courses are nodes, and prerequisites create directed edges between courses. 

It calculates the inDegree for each course to determine their dependencies.

The algorithm starts by enqueueing courses with no prerequisites into a queue and iteractively removes them while updating inDegrees of their dependent courses.

This process continues until all courses are their included in the result list or determined to be impossible due to cyclic dependencies.