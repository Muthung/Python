from collections import defaultdict, deque

class Solution():
    def findOrder(numCourses, prerequisites):
        # Create an adjacency list to represent the graph
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        # Build the graph and calculate in-degrees
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Initialize a queue with courses having no prerequisites
        queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
        result = []

        # Perform topological sorting
        while queue:
            course = queue.popleft()
            result.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        # If all courses are included, return the result; otherwise, return an empty array
        return result if len(result) == numCourses else []
