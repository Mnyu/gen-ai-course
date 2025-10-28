# Depth First Search Algorithm

def dfs(graph, start_node):
    visited = set()
    traversal_order = []
    
    def dfs_helper(node):
        visited.add(node)
        traversal_order.append(node)
        
        for neighbor in graph[node):
            if neighbor not in visited:
                dfs_helper(neighbor)
    
    dfs_helper(start_node)
    return traversal_order