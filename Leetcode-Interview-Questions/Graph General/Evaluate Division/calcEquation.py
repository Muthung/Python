from collections import defaultdict

class Solution(object):
    def calcEquation(equations, values, queries):
        graph = defaultdict(dict)
        
        # Build the graph
        for (numerator, denominator), value in zip(equations, values):
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value
        
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            
            if start == end:
                return 1.0
            
            visited.add(start)
            for neighbor, value in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return value * result
            
            visited.remove(start)
            return -1.0
        
        results = []
        
        for query in queries:
            start, end = query
            visited = set()
            result = dfs(start, end, visited)
            results.append(result)
        
        return results
