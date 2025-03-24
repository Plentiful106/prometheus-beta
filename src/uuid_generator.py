import os
import time
import hashlib

def generate_uuid():
    """
    Generate a Version 4 UUID without using external libraries.
    
    Returns:
        str: A unique identifier in standard UUID format (8-4-4-4-12 hexadecimal characters)
    
    The UUID is generated using:
    - Current timestamp
    - Process ID
    - Random bytes from os.urandom()
    
    Example:
        >>> uuid = generate_uuid()
        >>> len(uuid)
        36
        >>> uuid.count('-')
        4
    """
    # Get current timestamp and process ID for entropy
    timestamp = int(time.time() * 1000)
    pid = os.getpid()
    
    # Use os.urandom for cryptographically secure random bytes
    random_bytes = os.urandom(16)
    
    # Create a hash to mix the sources of entropy
    hash_input = f"{timestamp}{pid}".encode() + random_bytes
    hash_obj = hashlib.sha256(hash_input)
    
    # Convert hash to hex and truncate/format to UUID v4 format
    hex_uuid = hash_obj.hexdigest()[:32]
    
    # Format into standard UUID format
    return (
        f"{hex_uuid[:8]}-"
        f"{hex_uuid[8:12]}-"
        f"4{hex_uuid[12:15]}-"  # Version 4 UUID (starts with 4)
        f"8{hex_uuid[15:18]}-"  # Variant (starts with 8, 9, A, or B)
        f"{hex_uuid[18:30]}"
    )