def determine_football_match_winner(team1_players, team2_players, team1_goals, team2_goals):
    """
    Determine the winner of a football match based on goals scored and player conditions.

    Args:
        team1_players (int): Number of players on team 1
        team2_players (int): Number of players on team 2
        team1_goals (int): Number of goals scored by team 1
        team2_goals (int): Number of goals scored by team 2

    Returns:
        str: The result of the match ('Team 1 Wins', 'Team 2 Wins', or 'Draw')

    Raises:
        ValueError: If input values are invalid (negative or non-integer)
    """
    # Validate input types
    if not all(isinstance(x, int) for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("All inputs must be integers")

    # Validate non-negative inputs
    if any(x < 0 for x in [team1_players, team2_players, team1_goals, team2_goals]):
        raise ValueError("Input values cannot be negative")

    # Special case: If a team has 0 players, they lose
    if team1_players == 0:
        return "Team 2 Wins"
    if team2_players == 0:
        return "Team 1 Wins"

    # Compare goals to determine winner
    if team1_goals > team2_goals:
        return "Team 1 Wins"
    elif team2_goals > team1_goals:
        return "Team 2 Wins"
    else:
        return "Draw"