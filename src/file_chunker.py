import os
from typing import Union, Optional

def split_file_into_chunks(
    input_file: str, 
    chunk_size: Union[int, str] = 1024 * 1024,  # Default 1MB
    output_dir: Optional[str] = None,
    prefix: str = 'chunk_'
) -> list:
    """
    Split a large file into smaller chunks.

    Args:
        input_file (str): Path to the input file to be split.
        chunk_size (int or str): Size of each chunk in bytes. 
            Can be an integer or a string with units like '1MB', '500KB', etc.
        output_dir (str, optional): Directory to save chunks. 
            If None, uses the same directory as input file.
        prefix (str, optional): Prefix for chunk filenames. Defaults to 'chunk_'.

    Returns:
        list: List of paths to the created chunk files.

    Raises:
        FileNotFoundError: If input file does not exist.
        ValueError: If chunk size is invalid or less than 1.
    """
    # Validate input file
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file not found: {input_file}")

    # Parse chunk size if it's a string with units
    if isinstance(chunk_size, str):
        chunk_size = _parse_size_string(chunk_size)

    # Validate chunk size
    if chunk_size < 1:
        raise ValueError("Chunk size must be at least 1 byte")

    # Determine output directory
    if output_dir is None:
        output_dir = os.path.dirname(input_file) or '.'
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Prepare chunk file paths and tracking
    chunk_files = []
    base_filename = os.path.basename(input_file)

    # Perform file splitting
    with open(input_file, 'rb') as source_file:
        chunk_number = 1
        while True:
            # Read chunk
            chunk = source_file.read(chunk_size)
            
            # Break if no more data
            if not chunk:
                break

            # Create chunk filename
            chunk_filename = os.path.join(
                output_dir, 
                f'{prefix}{base_filename}_part{chunk_number}'
            )
            
            # Write chunk
            with open(chunk_filename, 'wb') as chunk_file:
                chunk_file.write(chunk)
            
            chunk_files.append(chunk_filename)
            chunk_number += 1

    return chunk_files

def _parse_size_string(size_str: str) -> int:
    """
    Parse a size string with units to bytes.

    Args:
        size_str (str): Size string like '1MB', '500KB', etc.

    Returns:
        int: Size in bytes.

    Raises:
        ValueError: If size string is invalid.
    """
    size_str = size_str.upper().strip()
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 * 1024,
        'GB': 1024 * 1024 * 1024,
        'TB': 1024 * 1024 * 1024 * 1024
    }

    # Check if string ends with a valid unit
    for unit, multiplier in units.items():
        if size_str.endswith(unit):
            try:
                # Remove unit and convert to int
                value = float(size_str[:-len(unit)])
                return int(value * multiplier)
            except ValueError:
                raise ValueError(f"Invalid size format: {size_str}")

    # If no unit found, try parsing as bytes
    try:
        return int(size_str)
    except ValueError:
        raise ValueError(f"Invalid size format: {size_str}")