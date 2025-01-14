def isValidBST(root):
    """
    :type root: Optional[TreeNode]
    :rtype: bool
    """
    def validate(node, low=float('-inf'), high=float('inf')):
      #Base case: Empty node is valid
        if not node:
            return True
          
        #Check if current node within correct range
        if node.val <= low or node.val >= high:
            return False

        #Use recursion to validate left and right subtrees
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)
    return validate(root)

    #time O(n) nodes in tree
    #space O(h) height of tree
