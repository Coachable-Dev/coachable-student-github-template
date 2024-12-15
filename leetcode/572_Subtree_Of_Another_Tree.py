def isSubtree(root, subRoot):
    """
    :type root: Optional[TreeNode]
    :type subRoot: Optional[TreeNode]
    :rtype: bool
    """
    #If root is None, can only return True if subRoot is also None.
    if not root:
        return not subRoot
    
    #Check if current tree matches or any subtree matches
    return (isIdentical(root, subRoot) or
            isSubtree(root.left, subRoot) or
            isSubtree(root.right, subRoot))
def isIdentical(tree1, tree2):
    #Both trees are None, they're identical
    if not tree1 and not tree2:
        return True

    #If one tree is None and other is not, they're not identical
    if not tree1 or not tree2:
        return False
    
    #Check current node values and recursively check left
    #right subtrees.
    return (tree1.val == tree2.val and
            isIdentical(tree1.left, tree2.left) and
            isIdentical(tree1.right, tree2.right))
    
    #time O(m*n) m for number of nodes in root,
    # n for number of nodes in subRoot
    #space O(h) for the height of the tree.
