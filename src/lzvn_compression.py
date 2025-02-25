"""
LZVN Compression Algorithm Implementation

This module provides a basic implementation of the LZVN (Lempel-Ziv Variable-length Numeric) 
compression algorithm, which is a variant of LZ compression.

Key characteristics:
- Designed for efficient compression of numeric sequences
- Uses variable-length encoding
- Supports basic compression and decompression
"""

def lzvn_compress(data):
    """
    Compress input data using the LZVN compression algorithm.
    
    Args:
        data (list or bytes-like): The input data to compress
    
    Returns:
        list: Compressed representation of the input data
    
    Raises:
        TypeError: If input is not a list or bytes-like object
        ValueError: If input data is empty
    """
    # Input validation
    if not data:
        raise ValueError("Input data cannot be empty")
    
    if not isinstance(data, (list, bytes, bytearray)):
        raise TypeError("Input must be a list, bytes, or bytearray")
    
    # Convert input to list if it's bytes-like
    if isinstance(data, (bytes, bytearray)):
        data = list(data)
    
    # Compression logic
    compressed = []
    i = 0
    while i < len(data):
        # Look for repeated sequences
        match_length = 0
        match_offset = 0
        
        # Search backwards for potential matches
        for j in range(max(0, i - 255), i):
            current_match_length = 0
            
            # Check match length
            while (i + current_match_length < len(data) and 
                   i + current_match_length < len(data) and 
                   data[i + current_match_length] == data[j + current_match_length]):
                current_match_length += 1
                
                # Limit match length to prevent overflow
                if current_match_length >= 255:
                    break
            
            # Update best match if found
            if current_match_length > match_length:
                match_length = current_match_length
                match_offset = i - j
        
        # Encode the result
        if match_length > 2:
            # Compression match found
            compressed.extend([
                match_length,  # Length of match
                match_offset   # Offset of match
            ])
            i += match_length
        else:
            # No match, store literal
            compressed.append(data[i])
            i += 1
    
    return compressed

def lzvn_decompress(compressed_data):
    """
    Decompress data compressed with LZVN algorithm.
    
    Args:
        compressed_data (list): Compressed data to decompress
    
    Returns:
        list: Decompressed original data
    
    Raises:
        TypeError: If input is not a list
        ValueError: If input data is invalid or corrupted
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Compressed data must be a list")
    
    if not compressed_data:
        raise ValueError("Compressed data cannot be empty")
    
    # Decompression logic
    decompressed = []
    i = 0
    
    while i < len(compressed_data):
        # Check if we have a match or literal
        if i + 1 < len(compressed_data) and isinstance(compressed_data[i], int) and isinstance(compressed_data[i+1], int):
            # This is a match (length, offset)
            match_length = compressed_data[i]
            match_offset = compressed_data[i+1]
            
            # Validate match parameters
            if match_length <= 0 or match_offset <= 0:
                raise ValueError(f"Invalid match parameters: length={match_length}, offset={match_offset}")
            
            # Copy matched sequence
            start = len(decompressed) - match_offset
            if start < 0:
                raise ValueError("Match offset exceeds decompressed data length")
            
            for j in range(match_length):
                if start + j < 0 or start + j >= len(decompressed):
                    raise ValueError("Invalid match sequence")
                decompressed.append(decompressed[start + j])
            
            i += 2  # Move past length and offset
        else:
            # Literal value
            decompressed.append(compressed_data[i])
            i += 1
    
    return decompressed