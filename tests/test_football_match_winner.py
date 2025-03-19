import pytest
from src.football_match_winner import determine_football_match_winner

def test_team1_wins_by_goals():
    """Test when Team 1 wins by scoring more goals"""
    assert determine_football_match_winner(11, 11, 3, 2) == "Team 1 Wins"

def test_team2_wins_by_goals():
    """Test when Team 2 wins by scoring more goals"""
    assert determine_football_match_winner(11, 11, 2, 3) == "Team 2 Wins"

def test_draw_equal_goals():
    """Test when the match is a draw with equal goals"""
    assert determine_football_match_winner(11, 11, 2, 2) == "Draw"

def test_team1_wins_by_zero_players():
    """Test when Team 2 has zero players"""
    assert determine_football_match_winner(11, 0, 2, 0) == "Team 1 Wins"

def test_team2_wins_by_zero_players():
    """Test when Team 1 has zero players"""
    assert determine_football_match_winner(0, 11, 0, 2) == "Team 2 Wins"

def test_invalid_negative_inputs():
    """Test that negative inputs raise a ValueError"""
    with pytest.raises(ValueError, match="Input values cannot be negative"):
        determine_football_match_winner(-1, 11, 2, 3)
    with pytest.raises(ValueError, match="Input values cannot be negative"):
        determine_football_match_winner(11, 11, -2, 3)

def test_invalid_input_types():
    """Test that non-integer inputs raise a ValueError"""
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11.5, 11, 2, 3)
    with pytest.raises(ValueError, match="All inputs must be integers"):
        determine_football_match_winner(11, 11, '2', 3)