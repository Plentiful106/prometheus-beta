import pytest
import ftplib
from unittest.mock import patch, MagicMock
from src.ftp_connection import establish_ftp_connection

class TestFTPConnection:
    def test_successful_connection(self):
        # Mock a successful FTP connection
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            connection, error = establish_ftp_connection(
                host='test.example.com', 
                username='testuser', 
                password='testpass'
            )
            
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_once_with(host='test.example.com', port=21)
            mock_instance.login.assert_called_once_with(user='testuser', passwd='testpass')

    def test_missing_parameters(self):
        # Test with missing parameters
        connection, error = establish_ftp_connection(
            host='', 
            username='', 
            password=''
        )
        
        assert connection is None
        assert "Missing required connection parameters" in error

    def test_connection_error(self):
        # Simulate FTP connection error
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            mock_instance.connect.side_effect = ftplib.error_perm("Connection failed")
            
            connection, error = establish_ftp_connection(
                host='invalid.example.com', 
                username='baduser', 
                password='badpass'
            )
            
            assert connection is None
            assert "FTP Connection Error" in error

    def test_custom_port(self):
        # Test connection with custom port
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            connection, error = establish_ftp_connection(
                host='test.example.com', 
                username='testuser', 
                password='testpass', 
                port=2121
            )
            
            assert connection is not None
            assert error is None
            mock_instance.connect.assert_called_once_with(host='test.example.com', port=2121)

    def test_timeout_handling(self):
        # Test connection with custom timeout
        with patch('ftplib.FTP') as mock_ftp:
            mock_instance = MagicMock()
            mock_ftp.return_value = mock_instance
            
            connection, error = establish_ftp_connection(
                host='test.example.com', 
                username='testuser', 
                password='testpass', 
                timeout=10
            )
            
            assert connection is not None
            assert error is None
            assert mock_ftp.call_args[1]['timeout'] == 10