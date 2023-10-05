def cloneGraph(node):
    if not node:
        return None

    visited = {}  # Dictionary to store visited nodes and their clones

    def dfs(original):
        if original in visited:
            return visited[original]

        # Create a clone of the current node
        clone = Node(original.val)
        visited[original] = clone

        # Recursively clone the neighbors
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)