def can_divide_subsequences(s: str) -> bool:
    """
    Determine if a string of lowercase English letters can be divided into 
    subsequences of at least 2 letters where each subsequence is either 
    all vowels or all consonants.

    Args:
        s (str): A string of lowercase English letters

    Returns:
        bool: True if the string can be divided into valid subsequences, 
              False otherwise

    Raises:
        ValueError: If the input contains characters other than lowercase letters
    """
    # Validate input
    if not s or not s.islower() or not s.isalpha():
        return False

    # Define vowels
    vowels = set('aeiou')

    # Helper function to check if a sequence is all vowels or all consonants
    def is_valid_subsequence(subseq):
        return len(subseq) > 1 and (
            all(char in vowels for char in subseq) or 
            all(char not in vowels for char in subseq)
        )

    # Dynamic programming approach to find valid division
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(2, n + 1):
        for j in range(0, i):
            # Check if the subsequence from j to i is valid
            if dp[j] and is_valid_subsequence(s[j:i]):
                dp[i] = True
                break

    return dp[n]