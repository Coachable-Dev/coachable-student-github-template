def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    "1,2,3,null,null,4,5"
    time O(n) for number of nodes
    space O(n) for recursive stack
    """
    def dfs(node):
        if not node:
            return "null"
        
        return str(node.val) + ',' + dfs(node.left) + ',' + dfs(node.right)
    
    return dfs(root)

def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    time O(n) size of string
    space O(n) recursion
    """
    def dfs(nodes):
        if not nodes:
            return None
        
        val = nodes.pop(0)

        if val == "null":
            return None

        node = TreeNode(int(val))

        node.left = dfs(nodes)
        node.right = dfs(nodes)

        return node
    
    if not data:
        return None
    
    nodes = data.split(',')
    return dfs(nodes)
