import os
import pytest
from cryptography.fernet import Fernet

from src.file_encryption import encrypt_file, generate_key

class TestFileEncryption:
    def setup_method(self):
        # Create a test file for encryption
        self.test_file_path = 'tests/test_file.txt'
        with open(self.test_file_path, 'wb') as f:
            f.write(b'This is a test file for encryption.')
    
    def teardown_method(self):
        # Clean up test files
        test_files = [
            self.test_file_path, 
            self.test_file_path + '.encrypted'
        ]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
    
    def test_generate_key(self):
        """Test key generation produces valid Fernet key"""
        key = generate_key()
        assert key is not None
        assert len(key) > 0
        
        # Validate it's a valid Fernet key
        try:
            Fernet(key)
        except Exception as e:
            pytest.fail(f"Generated key is not a valid Fernet key: {e}")
    
    def test_encrypt_file_default(self):
        """Test file encryption with default parameters"""
        key = encrypt_file(self.test_file_path)
        
        # Verify encrypted file exists
        encrypted_path = self.test_file_path + '.encrypted'
        assert os.path.exists(encrypted_path)
        
        # Verify encrypted content is different
        with open(self.test_file_path, 'rb') as original:
            with open(encrypted_path, 'rb') as encrypted:
                assert original.read() != encrypted.read()
    
    def test_encrypt_file_custom_output(self):
        """Test file encryption with custom output path"""
        custom_output = 'tests/custom_encrypted.txt'
        key = encrypt_file(self.test_file_path, output_path=custom_output)
        
        # Verify encrypted file exists at custom path
        assert os.path.exists(custom_output)
    
    def test_encrypt_file_custom_key(self):
        """Test file encryption with provided key"""
        custom_key = generate_key()
        key = encrypt_file(self.test_file_path, key=custom_key)
        
        # Verify returned key matches provided key
        assert key == custom_key
    
    def test_encrypt_nonexistent_file(self):
        """Test encryption of nonexistent file raises FileNotFoundError"""
        with pytest.raises(FileNotFoundError):
            encrypt_file('nonexistent_file.txt')
    
    def test_encrypt_invalid_input_path(self):
        """Test encryption with invalid input path raises ValueError"""
        with pytest.raises(ValueError):
            encrypt_file(None)
        with pytest.raises(ValueError):
            encrypt_file('')