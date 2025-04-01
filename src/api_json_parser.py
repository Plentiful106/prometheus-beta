import json
from typing import Any, Dict, Union

def parse_api_json_response(response: Union[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Parse a JSON response from an API.

    Args:
        response (Union[str, Dict[str, Any]]): The API response to parse.
            Can be a JSON string or an already parsed dictionary.

    Returns:
        Dict[str, Any]: Parsed JSON response as a dictionary.

    Raises:
        ValueError: If the response is invalid or cannot be parsed.
        TypeError: If the input is not a string or dictionary.
    """
    # Check input type
    if not isinstance(response, (str, dict)):
        raise TypeError("Response must be a JSON string or a dictionary")

    # If already a dictionary, return as-is
    if isinstance(response, dict):
        return response

    # If it's a string, try to parse
    try:
        return json.loads(response)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON string")