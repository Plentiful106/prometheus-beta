import brotli
import typing

def brotli_compress(data: typing.Union[str, bytes], quality: int = 11) -> bytes:
    """
    Compress data using Brotli compression algorithm.

    Args:
        data (str or bytes): The input data to compress.
        quality (int, optional): Compression quality (0-11). 
                                 0 is fastest, 11 is most compressed. 
                                 Defaults to 11 (highest compression).

    Returns:
        bytes: Compressed data.

    Raises:
        TypeError: If input is not str or bytes.
        ValueError: If compression quality is out of range.
    """
    # Validate input type
    if not isinstance(data, (str, bytes)):
        raise TypeError("Input must be str or bytes")
    
    # Convert str to bytes if needed
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # Validate compression quality
    if quality < 0 or quality > 11:
        raise ValueError("Compression quality must be between 0 and 11")
    
    # Compress the data
    return brotli.compress(data, quality)

def brotli_decompress(compressed_data: bytes) -> bytes:
    """
    Decompress Brotli compressed data.

    Args:
        compressed_data (bytes): Brotli compressed data.

    Returns:
        bytes: Decompressed data.

    Raises:
        TypeError: If input is not bytes.
        brotli.error: If decompression fails.
    """
    # Validate input type
    if not isinstance(compressed_data, bytes):
        raise TypeError("Input must be bytes")
    
    # Decompress the data
    return brotli.decompress(compressed_data)