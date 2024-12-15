def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: Optional[TreeNode]
    """
    #Create a hash map to store index of each value in inorder.
    #This allows 0(1) lookup of the index
    inorder_map = {val:idx for idx, val in enumerate(inorder)}

    #Track the current index in preorder array
    preorder_index = 0

    def array_to_tree(left, right):
        #If no elements to construct the tree
        if left > right:
            return None
        
        #Select current node from preorder traversal
        #The first element in preorder is always the root
        root_value = preorder[self.preorder_index]
        root = TreeNode(root_value)

        #Move to next element in preorder
        preorder_index += 1

        #Find the index of root in inorder to split
        #into left and right subtrees
        mid = inorder_map[root_value]

        #Use recursion to build left and right subtrees
        #For left, elements go from left to mid - 1
        #For right, elements go from mid + 1 to right
        root.left = array_to_tree(left, mid - 1)
        root.right = array_to_tree(mid + 1, right)

        return root

    #Call recursive helper with full range of inorder array
    return array_to_tree(0, len(inorder) - 1)

    #time O(n) for number of nodes in array,
    #O(1) lookups for hashmap
    #space O(n) recursive call stack in worst case
    #hash map to store inorder indices
