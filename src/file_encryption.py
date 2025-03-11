import os
from cryptography.fernet import Fernet

def generate_key() -> bytes:
    """
    Generate a new encryption key.
    
    Returns:
        bytes: A randomly generated encryption key
    """
    return Fernet.generate_key()

def encrypt_file(input_path: str, output_path: str = None, key: bytes = None) -> bytes:
    """
    Encrypt the contents of a file.
    
    Args:
        input_path (str): Path to the input file to be encrypted
        output_path (str, optional): Path to save the encrypted file. 
                                     If None, creates a .encrypted file next to input
        key (bytes, optional): Encryption key. If None, generates a new key
    
    Returns:
        bytes: The encryption key used
    
    Raises:
        FileNotFoundError: If the input file does not exist
        PermissionError: If there are permission issues reading/writing files
        ValueError: If input paths are invalid
    """
    # Validate input path
    if not input_path or not isinstance(input_path, str):
        raise ValueError("Invalid input path")
    
    # Check input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Generate key if not provided
    if key is None:
        key = generate_key()
    
    # Create Fernet cipher
    fernet = Fernet(key)
    
    # Read input file
    try:
        with open(input_path, 'rb') as file:
            file_data = file.read()
    except PermissionError:
        raise PermissionError(f"Permission denied reading input file: {input_path}")
    
    # Encrypt file contents
    encrypted_data = fernet.encrypt(file_data)
    
    # Determine output path
    if output_path is None:
        output_path = input_path + '.encrypted'
    
    # Write encrypted file
    try:
        with open(output_path, 'wb') as file:
            file.write(encrypted_data)
    except PermissionError:
        raise PermissionError(f"Permission denied writing encrypted file: {output_path}")
    
    return key