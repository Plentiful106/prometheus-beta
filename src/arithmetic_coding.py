from collections import Counter
from typing import List, Union, Dict, Any

def arithmetic_encode(data: Union[str, List[Any]]) -> Dict[str, Any]:
    """
    Perform Arithmetic Encoding on the input data.
    
    Args:
        data (Union[str, List[Any]]): Input data to be compressed
    
    Returns:
        Dict[str, Any]: A dictionary containing compression details
        - 'compressed_value': The final compressed value (float between 0 and 1)
        - 'frequency_table': Frequency distribution of symbols
    
    Raises:
        ValueError: If input data is empty
    """
    # Validate input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert input to list if it's a string
    if isinstance(data, str):
        data = list(data)
    
    # Create frequency table
    freq_table = Counter(data)
    total_symbols = len(data)
    
    # Calculate cumulative probabilities
    cumulative_prob = {}
    current_prob = 0
    for symbol, count in sorted(freq_table.items()):
        cumulative_prob[symbol] = {
            'low': current_prob / total_symbols,
            'high': (current_prob + count) / total_symbols
        }
        current_prob += count
    
    # Arithmetic encoding algorithm
    low = 0.0
    high = 1.0
    
    for symbol in data:
        # Calculate the range
        range_width = high - low
        
        # Update boundaries based on symbol probability
        symbol_range = cumulative_prob[symbol]
        high = low + range_width * symbol_range['high']
        low = low + range_width * symbol_range['low']
    
    # Final compressed value is the midpoint of the final range
    compressed_value = (low + high) / 2
    
    return {
        'compressed_value': compressed_value,
        'frequency_table': dict(freq_table)
    }

def arithmetic_decode(compressed_data: Dict[str, Any], original_length: int) -> Union[str, List[Any]]:
    """
    Perform Arithmetic Decoding to recover the original data.
    
    Args:
        compressed_data (Dict[str, Any]): Compression details from encoding
        original_length (int): Length of the original data
    
    Returns:
        Union[str, List[Any]]: Decoded data
    
    Raises:
        ValueError: If compression details are invalid
    """
    # Validate input
    if not compressed_data or 'compressed_value' not in compressed_data:
        raise ValueError("Invalid compressed data")
    
    compressed_value = compressed_data['compressed_value']
    freq_table = compressed_data['frequency_table']
    
    # Sort symbols by frequency for decoding
    sorted_symbols = sorted(freq_table.items(), key=lambda x: x[1], reverse=True)
    
    # Prepare decoding
    decoded_data = []
    low = 0.0
    high = 1.0
    
    # Reconstruct cumulative probabilities
    cumulative_prob = {}
    total_symbols = sum(freq_table.values())
    current_prob = 0
    
    for symbol, count in sorted(freq_table.items()):
        cumulative_prob[symbol] = {
            'low': current_prob / total_symbols,
            'high': (current_prob + count) / total_symbols
        }
        current_prob += count
    
    # Decode symbols
    for _ in range(original_length):
        for symbol, prob_range in cumulative_prob.items():
            symbol_low = prob_range['low']
            symbol_high = prob_range['high']
            
            # Check if compressed value falls in this symbol's range
            if symbol_low <= compressed_value < symbol_high:
                decoded_data.append(symbol)
                
                # Update range
                range_width = high - low
                high = low + range_width * prob_range['high']
                low = low + range_width * prob_range['low']
                break
    
    return decoded_data