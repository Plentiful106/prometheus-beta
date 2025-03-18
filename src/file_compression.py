import os
import zlib

def calculate_compression_ratio(file_path):
    """
    Calculate the compression ratio of a file.
    
    Args:
        file_path (str): Path to the file to be analyzed
    
    Returns:
        float: Compression ratio (compressed_size / original_size)
        
    Raises:
        FileNotFoundError: If the file does not exist
        ValueError: If the file is empty or cannot be read
    """
    # Validate file existence
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    # Check file size
    original_size = os.path.getsize(file_path)
    if original_size == 0:
        raise ValueError("Cannot calculate compression ratio for an empty file")
    
    # Read file content
    try:
        with open(file_path, 'rb') as f:
            file_content = f.read()
    except IOError:
        raise ValueError(f"Unable to read file: {file_path}")
    
    # Compress file content using zlib
    compressed_content = zlib.compress(file_content)
    compressed_size = len(compressed_content)
    
    # Calculate and return compression ratio
    compression_ratio = compressed_size / original_size
    return compression_ratio