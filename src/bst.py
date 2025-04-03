class TreeNode:
    """
    Represents a node in a Binary Search Tree.
    
    Attributes:
        key: The value/key stored in the node
        left: Left child node (containing smaller values)
        right: Right child node (containing larger values)
    """
    def __init__(self, key):
        """
        Initialize a new TreeNode.
        
        Args:
            key: The value to be stored in the node
        """
        self.key = key
        self.left = None
        self.right = None

def insert_bst_node(root, key):
    """
    Insert a new node with the given key into the Binary Search Tree.
    
    Args:
        root (TreeNode): The root of the current subtree
        key: The key to be inserted
    
    Returns:
        TreeNode: The root of the modified tree
    
    Raises:
        ValueError: If the key is None
    """
    # Validate input
    if key is None:
        raise ValueError("Cannot insert None as a key")
    
    # If the tree is empty, create a new root node
    if root is None:
        return TreeNode(key)
    
    # Recursively insert the node
    if key < root.key:
        # Insert in the left subtree
        root.left = insert_bst_node(root.left, key)
    elif key > root.key:
        # Insert in the right subtree
        root.right = insert_bst_node(root.right, key)
    # If key is equal, we don't insert duplicates (maintains BST property)
    
    return root