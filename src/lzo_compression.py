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
            # Encode match (length, offset)
            compressed.extend([
                best_match_length - 3,  # Length adjustment
                best_match_offset >> 8,  # High byte of offset
                best_match_offset & 0xFF,  # Low byte of offset
            ])
            i += best_match_length
        else:
            # Encode literal byte with flag
            if data[i] < 32:
                compressed.extend([0, data[i]])
            else:
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
        # Check for match or literal
        if compressed_data[i] < 32:
            # Match encoding
            if i + 2 >= len(compressed_data):
                # Incomplete match, treat as literal
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            try:
                # Decode match (length, offset)
                length = compressed_data[i] + 3
                offset = (compressed_data[i+1] << 8) | compressed_data[i+2]
                
                # Validate offset
                if offset == 0 or offset > len(decompressed):
                    # Invalid offset, treat as literal
                    decompressed.append(compressed_data[i])
                    i += 1
                    continue
                
                # Copy match from previous data
                for _ in range(length):
                    decompressed.append(decompressed[-offset])
                
                i += 3
            except IndexError:
                # Incomplete match data, treat as literal
                decompressed.append(compressed_data[i])
                i += 1
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed