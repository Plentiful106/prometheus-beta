import os
import pytest
import zipfile
import tempfile
import shutil

from src.zip_password_protector import create_password_protected_zip

def test_create_single_file_zip():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        # Create password-protected zip
        result_path = create_password_protected_zip([test_file_path], output_zip_path, 'testpass')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Open the zip and verify the content is encrypted
        with zipfile.ZipFile(result_path, 'r') as zf:
            # Read the encrypted content
            encrypted_content = zf.read('test_file.txt')
            
            # Check that the encrypted content is different from the original
            with open(test_file_path, 'rb') as f:
                original_content = f.read()
            
            assert encrypted_content != original_content

def test_create_directory_zip():
    # Create a temporary directory with nested files
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create nested directory structure
        os.makedirs(os.path.join(temp_dir, 'subdir'))
        with open(os.path.join(temp_dir, 'file1.txt'), 'w') as f:
            f.write('File 1 content')
        with open(os.path.join(temp_dir, 'subdir', 'file2.txt'), 'w') as f:
            f.write('File 2 content')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected_dir.zip')
        
        # Create password-protected zip
        result_path = create_password_protected_zip([temp_dir], output_zip_path, 'dirpass')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Open the zip and verify the content is encrypted
        with zipfile.ZipFile(result_path, 'r') as zf:
            # Read the encrypted content
            encrypted_content1 = zf.read('file1.txt')
            encrypted_content2 = zf.read('subdir/file2.txt')
            
            # Check that the encrypted content is different from the original
            with open(os.path.join(temp_dir, 'file1.txt'), 'rb') as f:
                original_content1 = f.read()
            with open(os.path.join(temp_dir, 'subdir', 'file2.txt'), 'rb') as f:
                original_content2 = f.read()
            
            assert encrypted_content1 != original_content1
            assert encrypted_content2 != original_content2

def test_multiple_sources_zip():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create multiple test files
        file1_path = os.path.join(temp_dir, 'file1.txt')
        file2_path = os.path.join(temp_dir, 'file2.txt')
        with open(file1_path, 'w') as f:
            f.write('First file')
        with open(file2_path, 'w') as f:
            f.write('Second file')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'multi_protected.zip')
        
        # Create password-protected zip
        result_path = create_password_protected_zip([file1_path, file2_path], output_zip_path, 'multipass')
        
        # Verify zip was created
        assert os.path.exists(result_path)
        
        # Open the zip and verify the content is encrypted
        with zipfile.ZipFile(result_path, 'r') as zf:
            # Read the encrypted content
            encrypted_content1 = zf.read('file1.txt')
            encrypted_content2 = zf.read('file2.txt')
            
            # Check that the encrypted content is different from the original
            with open(file1_path, 'rb') as f:
                original_content1 = f.read()
            with open(file2_path, 'rb') as f:
                original_content2 = f.read()
            
            assert encrypted_content1 != original_content1
            assert encrypted_content2 != original_content2

def test_invalid_inputs():
    # Test empty source paths
    with pytest.raises(ValueError, match="At least one source path must be provided"):
        create_password_protected_zip([], 'test.zip', 'password')
    
    # Test invalid password (too short)
    with pytest.raises(ValueError, match="Password must be a string of at least 4 characters"):
        create_password_protected_zip(['test.txt'], 'test.zip', '123')
    
    # Test non-existent file
    with pytest.raises(FileNotFoundError):
        create_password_protected_zip(['/path/to/nonexistent/file'], 'test.zip', 'password')

def test_try_open_wrong_password():
    # Create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Create a test file
        test_file_path = os.path.join(temp_dir, 'test_file.txt')
        with open(test_file_path, 'w') as f:
            f.write('Test content')
        
        # Output zip path
        output_zip_path = os.path.join(temp_dir, 'protected.zip')
        
        # Create password-protected zip
        create_password_protected_zip([test_file_path], output_zip_path, 'correctpass')
        
        # Verify the content is different
        with open(test_file_path, 'rb') as f:
            original_content = f.read()
        
        with zipfile.ZipFile(output_zip_path, 'r') as zf:
            # Attempt to read with wrong password
            encrypted_content = zf.read('test_file.txt')
            assert encrypted_content != original_content