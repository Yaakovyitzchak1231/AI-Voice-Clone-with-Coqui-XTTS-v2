"""
Utility functions for audio processing and file handling.
"""

import os
from typing import Optional


def validate_audio_file(file_path: str) -> bool:
    """
    Validate if the audio file exists and has correct format.
    
    Args:
        file_path: Path to audio file.
        
    Returns:
        True if file is valid, False otherwise.
    """
    if not os.path.exists(file_path):
        return False
        
    valid_extensions = ['.wav', '.mp3', '.m4a', '.flac']
    file_ext = os.path.splitext(file_path)[1].lower()
    
    return file_ext in valid_extensions


def ensure_output_dir(output_path: str) -> None:
    """
    Ensure the output directory exists.
    
    Args:
        output_path: Path to output file.
    """
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
