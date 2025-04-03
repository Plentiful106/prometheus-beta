import pytest
from src.bst import TreeNode, insert_bst_node

def test_insert_into_empty_tree():
    """Test inserting into an empty tree creates a new root node"""
    root = insert_bst_node(None, 5)
    assert root is not None
    assert root.key == 5
    assert root.left is None
    assert root.right is None

def test_insert_left_subtree():
    """Test inserting a smaller key goes to the left subtree"""
    root = insert_bst_node(None, 10)
    root = insert_bst_node(root, 5)
    
    assert root.key == 10
    assert root.left is not None
    assert root.left.key == 5
    assert root.right is None

def test_insert_right_subtree():
    """Test inserting a larger key goes to the right subtree"""
    root = insert_bst_node(None, 10)
    root = insert_bst_node(root, 15)
    
    assert root.key == 10
    assert root.right is not None
    assert root.right.key == 15
    assert root.left is None

def test_insert_multiple_nodes():
    """Test inserting multiple nodes maintains BST properties"""
    root = None
    # Insert in various orders
    values = [10, 5, 15, 3, 7, 12, 18]
    for val in values:
        root = insert_bst_node(root, val)
    
    # Validate tree structure
    assert root.key == 10
    assert root.left.key == 5
    assert root.right.key == 15
    assert root.left.left.key == 3
    assert root.left.right.key == 7
    assert root.right.left.key == 12
    assert root.right.right.key == 18

def test_insert_duplicate_key():
    """Test that duplicate keys are not inserted"""
    root = insert_bst_node(None, 10)
    root = insert_bst_node(root, 10)
    
    # Ensure the tree remains unchanged
    assert root.key == 10
    assert root.left is None
    assert root.right is None

def test_insert_none_raises_error():
    """Test that inserting None raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot insert None as a key"):
        insert_bst_node(None, None)

def test_insert_deep_tree():
    """Test creating a deeper tree with multiple levels"""
    root = None
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        root = insert_bst_node(root, val)
    
    # Validate deeper tree structure
    assert root.key == 50
    assert root.left.key == 30
    assert root.right.key == 70
    assert root.left.left.key == 20
    assert root.left.right.key == 40
    assert root.right.left.key == 60
    assert root.right.right.key == 80