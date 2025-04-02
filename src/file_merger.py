import os
from typing import List, Union

def merge_files(input_files: List[str], output_file: str, delimiter: str = '\n\n') -> None:
    """
    Merge multiple files into a single output file.

    Args:
        input_files (List[str]): List of paths to input files to be merged.
        output_file (str): Path to the output merged file.
        delimiter (str, optional): Delimiter to use between merged file contents. 
                                   Defaults to double newline.

    Raises:
        FileNotFoundError: If any of the input files do not exist.
        TypeError: If input_files is not a list or contains non-string elements.
        ValueError: If input_files is empty.
    """
    # Validate input
    if not isinstance(input_files, list):
        raise TypeError("input_files must be a list of file paths")
    
    if len(input_files) == 0:
        raise ValueError("input_files cannot be empty")
    
    if not all(isinstance(f, str) for f in input_files):
        raise TypeError("All elements in input_files must be strings")

    # Check file existence
    for file_path in input_files:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

    # Read and merge file contents
    merged_contents = []
    for file_path in input_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            merged_contents.append(f.read().strip())

    # Write merged contents to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(delimiter.join(merged_contents))