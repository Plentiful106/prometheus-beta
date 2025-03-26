class TreeNode:
    """
    A class representing a node in a binary tree.
    
    Attributes:
        value (int): The value stored in the node
        left (TreeNode, optional): Left child node, defaults to None
        right (TreeNode, optional): Right child node, defaults to None
    """
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs_ascending(root):
    """
    Perform a depth-first search on a binary tree and return node values in ascending order.
    
    Args:
        root (TreeNode): The root node of the binary tree
    
    Returns:
        list: A list of node values in ascending order
    
    Raises:
        TypeError: If the input is not a TreeNode or None
    """
    # Handle edge cases
    if root is None:
        return []
    
    # Validate input type
    if not isinstance(root, TreeNode):
        raise TypeError("Input must be a TreeNode or None")
    
    # In-order traversal (left-root-right) ensures ascending order for a BST
    result = []
    
    def _inorder_traverse(node):
        """
        Recursive helper function for in-order traversal
        
        Args:
            node (TreeNode): Current node being traversed
        """
        if node is None:
            return
        
        # Traverse left subtree
        _inorder_traverse(node.left)
        
        # Add current node's value
        result.append(node.value)
        
        # Traverse right subtree
        _inorder_traverse(node.right)
    
    # Start the traversal
    _inorder_traverse(root)
    
    return result