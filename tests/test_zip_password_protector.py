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
        
        # Try to open with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'testpass')
            contents = zf.read('test_file.txt')
            assert contents == b'Test content'

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
        
        # Try to open with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'dirpass')
            contents1 = zf.read('file1.txt')
            contents2 = zf.read('subdir/file2.txt')
            assert contents1 == b'File 1 content'
            assert contents2 == b'File 2 content'

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
        
        # Try to open with correct password
        with zipfile.ZipFile(result_path, 'r') as zf:
            zf.setpassword(b'multipass')
            contents1 = zf.read('file1.txt')
            contents2 = zf.read('file2.txt')
            assert contents1 == b'First file'
            assert contents2 == b'Second file'

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
        
        # Try to open with incorrect password
        with zipfile.ZipFile(output_zip_path, 'r') as zf:
            zf.setpassword(b'wrongpass')
            # Test for decryption failure
            with pytest.raises(Exception, match="(?i)pass"):
                raw_data = zf.read('test_file.txt')