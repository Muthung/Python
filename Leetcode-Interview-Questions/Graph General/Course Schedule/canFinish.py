from collections import defaultdict

class Solution():
    def canFinish(numCourses, prerequisites):
        # Create a graph representation where each course is a node and prerequisites are edges.
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # Initialize a list to keep track of visited nodes during DFS.
        visited = [0] * numCourses

        def is_cyclic(node):
            if visited[node] == -1:
                return True  # Found a cycle.
            if visited[node] == 1:
                return False  # This node has already been visited and is not part of a cycle.

            visited[node] = -1  # Mark the node as visited in the current DFS traversal.
            for neighbor in graph[node]:
                if is_cyclic(neighbor):
                    return True

            visited[node] = 1  # Mark the node as visited and not part of a cycle.
            return False

        # Check for cycles in the graph using DFS.
        for course in range(numCourses):
            if is_cyclic(course):
                return False

        return True