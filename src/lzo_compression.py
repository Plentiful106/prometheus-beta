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
    
    # Compression variables
    compressed = bytearray()
    window_size = 4096  # Default sliding window size
    
    # Main compression loop
    i = 0
    while i < len(data):
        # Find longest match in previous data
        best_match_length = 0
        best_match_offset = 0
        
        # Look back to a maximum of window_size previous bytes
        max_lookback = min(i, window_size)
        
        # Search for the longest match
        for lookback_pos in range(1, max_lookback + 1):
            match_length = 0
            
            # Check how long the match continues
            while (i + match_length < len(data) and 
                   match_length < 255 and 
                   data[i + match_length] == data[i - lookback_pos + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = lookback_pos
        
        # Encode the match or literal
        if best_match_length > 2:
            # Encode match (offset, length)
            compressed.extend([
                best_match_offset >> 8,  # High byte of offset
                best_match_offset & 0xFF,  # Low byte of offset
                best_match_length - 3  # Length adjustment
            ])
            i += best_match_length
        else:
            # Encode literal byte
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
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check if we can read next bytes
        if i + 2 >= len(compressed_data):
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
            continue
        
        # Check for match or literal
        if compressed_data[i] < 32:  # Match encoding
            # Ensure sufficient data for match
            if i + 2 >= len(compressed_data):
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Reconstruct offset and length
            try:
                offset = (compressed_data[i] << 8) | compressed_data[i+1]
                length = compressed_data[i+2] + 3
            except IndexError:
                # Treat as literal if index is out of bounds
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Validate offset and length
            if offset == 0 or offset > len(decompressed):
                # Treat as literal if invalid offset
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Copy match from previous data
            for _ in range(length):
                decompressed.append(decompressed[-offset])
            
            i += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed