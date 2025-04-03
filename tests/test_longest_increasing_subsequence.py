import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

# ... (previous tests remain the same)

def test_negative_numbers():
    """Test a sequence with negative numbers."""
    assert find_longest_increasing_subsequence([-5, -4, -3, -2, -1]) == 5
    assert find_longest_increasing_subsequence([-1, 0, 2, -3, 4, 5]) == 4
    assert find_longest_increasing_subsequence([-10, -5, 1, 2, 3]) == 4