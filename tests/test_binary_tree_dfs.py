import pytest
from src.binary_tree_dfs import TreeNode, dfs_ascending

def test_empty_tree():
    """Test that an empty tree returns an empty list"""
    assert dfs_ascending(None) == []

def test_single_node_tree():
    """Test a tree with a single node"""
    root = TreeNode(5)
    assert dfs_ascending(root) == [5]

def test_balanced_binary_search_tree():
    """Test a balanced binary search tree"""
    #       5
    #     /   \
    #    3     7
    #   / \   / \
    #  1   4 6   8
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)
    
    assert dfs_ascending(root) == [1, 3, 4, 5, 6, 7, 8]

def test_left_skewed_tree():
    """Test a left-skewed tree"""
    #   5
    #  /
    # 3
    # /
    # 1
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    
    assert dfs_ascending(root) == [1, 3, 5]

def test_right_skewed_tree():
    """Test a right-skewed tree"""
    # 1
    #  \
    #   3
    #    \
    #     5
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.right = TreeNode(5)
    
    assert dfs_ascending(root) == [1, 3, 5]

def test_invalid_input():
    """Test that invalid input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending("not a tree")
    
    with pytest.raises(TypeError, match="Input must be a TreeNode or None"):
        dfs_ascending(42)