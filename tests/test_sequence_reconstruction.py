import pytest
from src.sequence_reconstruction import min_sequence_reconstruction_ops

def test_no_operations_needed():
    """Test when sequences are identical"""
    assert min_sequence_reconstruction_ops([1, 2, 3], [1, 2, 3]) == 0

def test_all_removals():
    """Test when current sequence needs complete removal"""
    assert min_sequence_reconstruction_ops([1, 2, 3], [4, 5, 6]) == 6

def test_all_insertions():
    """Test when sequence needs complete insertion"""
    assert min_sequence_reconstruction_ops([1, 2, 3], []) == 3

def test_mixed_operations():
    """Test a mix of insertions and removals"""
    assert min_sequence_reconstruction_ops([1, 2, 3, 4], [2, 5]) == 3

def test_duplicates_handling():
    """Test with sequences containing duplicates"""
    assert min_sequence_reconstruction_ops([1, 1, 2, 2], [1, 3, 3]) == 3

def test_empty_sequences():
    """Test with empty sequences"""
    assert min_sequence_reconstruction_ops([], []) == 0
    assert min_sequence_reconstruction_ops([1, 2], []) == 2
    assert min_sequence_reconstruction_ops([], [1, 2]) == 2

def test_invalid_input_types():
    """Test raising error for invalid input types"""
    with pytest.raises(ValueError):
        min_sequence_reconstruction_ops("not a list", [1, 2])
    
    with pytest.raises(ValueError):
        min_sequence_reconstruction_ops([1, 2], "not a list")

def test_non_hashable_input():
    """Test handling of non-hashable list elements"""
    with pytest.raises(ValueError):
        min_sequence_reconstruction_ops([[1]], [[2]])