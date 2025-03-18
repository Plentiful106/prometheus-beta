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
    lookback_buffer = bytearray()
    
    # Main compression loop
    i = 0
    while i < len(data):
        # Find longest match in lookback buffer
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the lookback buffer for the longest match
        for offset in range(1, min(len(lookback_buffer) + 1, window_size + 1)):
            # Bounds check for lookback_buffer
            current_buffer_pos = len(lookback_buffer)
            if current_buffer_pos < offset:
                continue
            
            match_length = 0
            
            # Check how long the match continues
            while (i + match_length < len(data) and 
                   match_length < 255 and 
                   data[i + match_length] == lookback_buffer[current_buffer_pos - offset + match_length]):
                match_length += 1
            
            # Update best match if found
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = offset
        
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
        
        # Update lookback buffer
        if i > 0:
            lookback_buffer.append(data[i-1])
        
        # Trim lookback buffer if it exceeds window size
        if len(lookback_buffer) > window_size:
            lookback_buffer = lookback_buffer[-window_size:]
    
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
            # Reconstruct offset and length
            offset = (compressed_data[i] << 8) | compressed_data[i+1]
            length = compressed_data[i+2] + 3
            
            # Validate offset and length
            if offset == 0 or len(decompressed) == 0:
                # For first iteration or invalid offset, treat as literal
                decompressed.append(compressed_data[i])
                i += 1
                continue
            
            # Adjust offset to prevent out of bounds
            offset = min(offset, len(decompressed))
            
            # Copy match from previous data
            for _ in range(length):
                decompressed.append(decompressed[-offset])
            
            i += 3
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed