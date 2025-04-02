"""
Module for comparing files to check if they are identical.

This module provides a function to compare two files and determine 
if they have identical content.
"""

import os
import hashlib


def are_files_identical(file1_path: str, file2_path: str) -> bool:
    """
    Compare two files to check if they are identical.

    Args:
        file1_path (str): Path to the first file
        file2_path (str): Path to the second file

    Returns:
        bool: True if files are identical, False otherwise

    Raises:
        FileNotFoundError: If either file does not exist
        PermissionError: If there are permission issues reading the files
        IsADirectoryError: If either path is a directory instead of a file
    """
    # Check if files exist
    if not os.path.isfile(file1_path):
        raise FileNotFoundError(f"First file not found: {file1_path}")
    if not os.path.isfile(file2_path):
        raise FileNotFoundError(f"Second file not found: {file2_path}")

    # Check file sizes first (quick initial comparison)
    if os.path.getsize(file1_path) != os.path.getsize(file2_path):
        return False

    # Compare file contents using hash
    def file_hash(filepath):
        """Generate SHA-256 hash for a file."""
        hasher = hashlib.sha256()
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()

    return file_hash(file1_path) == file_hash(file2_path)