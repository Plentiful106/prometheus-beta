"""
LZJH (Lempel-Ziv-Jones-Hussmann) Compression Algorithm Implementation

This module provides functions for LZJH compression and decompression.
LZJH is a variant of LZ compression that uses a specific approach to dictionary building.
"""

def compress(data):
    """
    Compress the input data using the LZJH compression algorithm.
    
    Args:
        data (bytes or str): The input data to compress.
    
    Returns:
        bytes: Compressed data.
    
    Raises:
        TypeError: If input is not bytes or str.
        ValueError: If input is empty.
    """
    # Validate input
    if data is None:
        raise TypeError("Input cannot be None")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Convert to bytes if input is a string
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    if not isinstance(data, bytes):
        raise TypeError("Input must be bytes or str")
    
    # Initialize compression variables
    dictionary = {bytes([i]): i for i in range(256)}
    next_code = 256
    current_phrase = bytes([data[0]])
    result = bytearray()
    
    # Compression algorithm
    for byte in data[1:]:
        # Create a new phrase by extending the current phrase
        new_phrase = current_phrase + bytes([byte])
        
        if new_phrase in dictionary:
            # If the new phrase exists in the dictionary, continue building it
            current_phrase = new_phrase
        else:
            # Output the code for the current phrase
            code = dictionary[current_phrase]
            result.extend(code.to_bytes(2, byteorder='big'))
            
            # Add the new phrase to the dictionary if room allows
            if next_code < 65536:  # Limit dictionary size
                dictionary[new_phrase] = next_code
                next_code += 1
            
            # Reset current phrase to the current byte
            current_phrase = bytes([byte])
    
    # Output the last phrase
    code = dictionary[current_phrase]
    result.extend(code.to_bytes(2, byteorder='big'))
    
    return bytes(result)

def decompress(compressed_data):
    """
    Decompress data that was compressed using the LZJH algorithm.
    
    Args:
        compressed_data (bytes): The compressed input data.
    
    Returns:
        bytes: Decompressed data.
    
    Raises:
        TypeError: If input is not bytes.
        ValueError: If input is empty or invalid.
    """
    # Validate input
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Initialize decompression variables
    dictionary = {i: bytes([i]) for i in range(256)}
    next_code = 256
    result = bytearray()
    
    # Read first code (2 bytes)
    current_code = int.from_bytes(compressed_data[:2], byteorder='big')
    current_phrase = dictionary[current_code]
    result.extend(current_phrase)
    
    # Decompression algorithm
    for i in range(2, len(compressed_data), 2):
        # Retrieve next code from compressed data
        try:
            code = int.from_bytes(compressed_data[i:i+2], byteorder='big')
        except IndexError:
            raise ValueError("Invalid compressed data length")
        
        # Retrieve phrase for current code
        if code in dictionary:
            new_phrase = dictionary[code]
        elif code == next_code:
            # Special case: new phrase is previous phrase + its first byte
            new_phrase = current_phrase + bytes([current_phrase[0]])
        else:
            raise ValueError(f"Invalid compressed data at code {code}")
        
        # Add new phrase to result
        result.extend(new_phrase)
        
        # Update dictionary if room allows
        if next_code < 65536:
            dictionary[next_code] = current_phrase + bytes([new_phrase[0]])
            next_code += 1
        
        # Update current phrase
        current_phrase = new_phrase
    
    return bytes(result)