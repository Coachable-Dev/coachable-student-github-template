def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    #create a dictionary to store node copies as we make them
    clone_map = {}

    def dfs(node):
        if not node:
            return None
        
        #If we've already cloned this node, return the clone
        if node in clone_map:
            return clone_map[node]
        
        #Create a new node with same value
        clone_node = Node(node.val)
        #Add to clone map before exploring neighbors(for cycles)
        clone_map[node] = clone_node

        #Clone all neighbors recursively
        for neighbor in node.neighbors:
            clone_node.neighbors.append(dfs(neighbor))
        
        return clone_node
    return dfs(node)

    #time O(V + E)
    #space O(V)
