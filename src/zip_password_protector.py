import os
import zipfile
import stat

def create_password_protected_zip(source_paths, output_zip_path, password):
    """
    Create a password-protected ZIP file from given source files or directories.

    Args:
        source_paths (list): List of file or directory paths to be added to the zip
        output_zip_path (str): Path where the password-protected zip will be saved
        password (str): Password to protect the zip file

    Raises:
        ValueError: If source_paths is empty or password is invalid
        IOError: If there are issues reading source files or creating zip
    """
    # Validate inputs
    if not source_paths:
        raise ValueError("At least one source path must be provided")
    
    if not isinstance(password, str) or len(password) < 4:
        raise ValueError("Password must be a string of at least 4 characters")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_zip_path), exist_ok=True)
    
    # Create a ZipFile with encryption
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add each source path to the zip
            for source_path in source_paths:
                # Validate source path exists
                if not os.path.exists(source_path):
                    raise FileNotFoundError(f"Source path not found: {source_path}")
                
                # If it's a directory, walk through and add all files
                if os.path.isdir(source_path):
                    for root, _, files in os.walk(source_path):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, source_path)
                            
                            # Open and read file contents
                            with open(file_path, 'rb') as f:
                                file_content = f.read()
                            
                            # Create a new ZipInfo with password protection
                            zinfo = zipfile.ZipInfo(arcname)
                            zinfo.flag_bits |= 0x1  # Turn on encryption flag
                            
                            # Write the encrypted file
                            zipf.writestr(zinfo, file_content, zipfile.ZIP_DEFLATED, pwd=password.encode())
                else:
                    # If it's a single file
                    # Open and read file contents
                    with open(source_path, 'rb') as f:
                        file_content = f.read()
                    
                    # Create a new ZipInfo with password protection
                    zinfo = zipfile.ZipInfo(os.path.basename(source_path))
                    zinfo.flag_bits |= 0x1  # Turn on encryption flag
                    
                    # Write the encrypted file
                    zipf.writestr(zinfo, file_content, zipfile.ZIP_DEFLATED, pwd=password.encode())
    
    except Exception as e:
        raise IOError(f"Error creating password-protected zip: {str(e)}")
    
    return output_zip_path