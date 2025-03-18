"""
Lempel-Ziv-Oberhumer (LZO) Compression Implementation

This module provides a simple implementation of LZO compression algorithm.
Note: This is a basic implementation and not a full, optimized LZO library.
"""

def lzo_compress(data):
    """
    Compress input data using a basic LZO-inspired compression algorithm.
    
    Args:
        data (bytes or bytearray): Input data to compress
    
    Returns:
        bytearray: Compressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty
    """
    # Input validation
    if not isinstance(data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Simple heuristic to detect highly random data that won't compress
    unique_chars = len(set(data))
    is_random = unique_chars > len(data) * 0.9
    
    # If data is too random, return original with a no-op flag
    if is_random or len(data) < 32:
        compressed = bytearray([0xFF])  # No-op flag
        compressed.extend(data)
        return compressed
    
    # Compression variables
    compressed = bytearray()
    window_size = 4096  # Default sliding window size
    
    # Main compression loop
    i = 0
    while i < len(data):
        # Literal flag if no good match found
        found_match = False
        
        # Look back to a maximum of window_size previous bytes 
        max_lookback = min(i, window_size)
        for j in range(1, max_lookback + 1):
            match_length = 0
            while (i + match_length < len(data) and 
                   match_length < 255 and 
                   data[i + match_length] == data[i - j + match_length]):
                match_length += 1
            
            # If match is found
            if match_length > 2:
                # Compressed match
                compressed.extend([
                    match_length,  # Length of match
                    j >> 8,  # High byte of offset
                    j & 0xFF  # Low byte of offset
                ])
                i += match_length
                found_match = True
                break
        
        # If no match found, add literal
        if not found_match:
            compressed.append(data[i])
            i += 1
    
    return compressed

def lzo_decompress(compressed_data):
    """
    Decompress data compressed with the corresponding LZO compression method.
    
    Args:
        compressed_data (bytes or bytearray): Compressed input data
    
    Returns:
        bytearray: Decompressed data
    
    Raises:
        TypeError: If input is not bytes or bytearray
        ValueError: If input data is empty or invalid
    """
    # Input validation
    if not isinstance(compressed_data, (bytes, bytearray)):
        raise TypeError("Input must be bytes or bytearray")
    
    if not compressed_data:
        raise ValueError("Input data cannot be empty")
    
    # Check for no-op flag 0xFF indicating uncompressed data
    if compressed_data[0] == 0xFF and len(compressed_data) > 1:
        return bytearray(compressed_data[1:])
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Ensure we have data to read
        if i + 2 >= len(compressed_data):
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        # Check if it's a match or literal
        if compressed_data[i] > 2:
            # Match encoding
            match_length = compressed_data[i]
            try:
                offset = (compressed_data[i+1] << 8) | compressed_data[i+2]
            except IndexError:
                # Not enough bytes, treat as literal
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Validate match
            if offset == 0 or offset > len(decompressed):
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Reconstruct match
            for _ in range(match_length):
                try:
                    decompressed.append(decompressed[-offset])
                except IndexError:
                    # Unexpected end, stop compression
                    break
            
            i += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed