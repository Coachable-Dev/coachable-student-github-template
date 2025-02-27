def maxPathSum(root):
    """
    :type root: Optional[TreeNode]
    :rtype: int
    """
    max_sum = float('-inf')

    def max_gain(node):
        '''
        Calculates the max of a subtree.
        1. updates the global max path sum
        2. Returns the max path sum through the node
        that can be extended to its parent.
        '''
        #Base case: if node is None return 0.
        if not node:
            return 0
        
        #Use recursion for left and right subtrees
        #use max with 0 to ignore neg elements.
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        #Compute max path sum through this node
        current_path_sum = node.val + left_gain + right_gain
        #Update global max if current path longer
        max_sum = max(max_sum, current_path_sum)

        #Return max gain
        return node.val + max(left_gain, right_gain)
    
    #start recursion
    max_gain(root)

    return max_sum

    #time O(n) for number of nodes
    #space O(h) for height of tree
