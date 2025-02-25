import pytest
from src.ball_stack_sorter import BallStackSorter

def test_valid_initial_sorting():
    """Test sorting when stacks are already sorted"""
    sorter = BallStackSorter(
        red_stack=['Red', 'Red', 'Red'],
        blue_stack=['Blue', 'Blue', 'Blue'],
        green_stack=['Green', 'Green', 'Green']
    )
    assert sorter.sort() == True

def test_mixed_stacks_sorting():
    """Test sorting mixed color stacks"""
    sorter = BallStackSorter(
        red_stack=['Red', 'Blue', 'Green'],
        blue_stack=['Blue', 'Green', 'Red'],
        green_stack=['Green', 'Red', 'Blue']
    )
    assert sorter.sort() == True

def test_unequal_stack_lengths():
    """Test that unequal stack lengths raise a ValueError"""
    with pytest.raises(ValueError):
        BallStackSorter(
            red_stack=['Red', 'Red'],
            blue_stack=['Blue', 'Blue', 'Blue'],
            green_stack=['Green', 'Green', 'Green']
        )

def test_invalid_colors():
    """Test that invalid colors raise a ValueError"""
    with pytest.raises(ValueError):
        BallStackSorter(
            red_stack=['Red', 'Yellow', 'Green'],
            blue_stack=['Blue', 'Blue', 'Blue'],
            green_stack=['Green', 'Green', 'Green']
        )

def test_nearly_impossible_sorting():
    """Test a challenging sorting scenario"""
    sorter = BallStackSorter(
        red_stack=['Red', 'Blue', 'Red'],
        blue_stack=['Green', 'Red', 'Blue'],
        green_stack=['Blue', 'Green', 'Green']
    )
    assert sorter.sort() == True

def test_color_distribution():
    """Test sorting and verify final color distribution"""
    sorter = BallStackSorter(
        red_stack=['Red', 'Blue', 'Green'],
        blue_stack=['Blue', 'Green', 'Red'],
        green_stack=['Green', 'Red', 'Blue']
    )
    sorter.sort()
    
    # Verify that each stack is now a single color
    assert len(set(sorter.stacks['Red'])) == 1
    assert len(set(sorter.stacks['Blue'])) == 1
    assert len(set(sorter.stacks['Green'])) == 1