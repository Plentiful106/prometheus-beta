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
    
    # Special handling for very short or non-compressible data
    if len(data) < 64 or len(set(data)) > len(data) * 0.9:
        return bytearray(data)
    
    # Compression variables
    compressed = bytearray()
    window_size = 4096  # Default sliding window size
    
    # Main compression loop
    i = 0
    while i < len(data):
        # Try to find match in previous window
        best_match_length = 0
        best_match_offset = 0
        
        # Search back in the previous window
        max_lookback = min(i, window_size)
        for j in range(max(0, i - max_lookback), i):
            match_length = 0
            
            # Find match length
            while (i + match_length < len(data) and 
                   match_length < 255 and 
                   data[i + match_length] == data[j + match_length]):
                match_length += 1
            
            # Update best match
            if match_length > best_match_length:
                best_match_length = match_length
                best_match_offset = i - j
        
        # Compress based on match
        if best_match_length > 3:
            # Match with offset and length
            compressed.extend([
                best_match_length - 3,  # Length adjustment 
                best_match_offset >> 8,  # High byte of offset
                best_match_offset & 0xFF  # Low byte of offset
            ])
            i += best_match_length
        else:
            # Literal byte
            compressed.append(data[i])
            i += 1
    
    # Return original if compressed data isn't beneficial
    return compressed if len(compressed) < len(data) * 0.9 else bytearray(data)

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
    
    # If data seems uncompressed, return it
    if len(compressed_data) <= 10:
        return bytearray(compressed_data)
    
    # Decompression variables
    decompressed = bytearray()
    i = 0
    
    while i < len(compressed_data):
        # Check for match or literal
        if i + 2 < len(compressed_data) and compressed_data[i] < 32:
            # Match encoding
            try:
                match_length = compressed_data[i] + 3
                offset = (compressed_data[i+1] << 8) | compressed_data[i+2]
                
                # Validate match parameters
                if offset == 0 or offset > len(decompressed):
                    # Invalid match, treat as literal
                    decompressed.append(compressed_data[i])
                    i += 1
                    continue
                
                # Copy match bytes
                for _ in range(match_length):
                    if len(decompressed) < offset:
                        break
                    decompressed.append(decompressed[-offset])
                
                i += 3
            except IndexError:
                # Incomplete match
                decompressed.append(compressed_data[i])
                i += 1
        else:
            # Literal byte
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed