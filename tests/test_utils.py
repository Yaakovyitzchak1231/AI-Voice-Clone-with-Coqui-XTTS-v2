"""
Unit tests for utility functions.
"""

import os
import pytest
import tempfile
from xtts_voice_clone.utils import validate_audio_file, ensure_output_dir


class TestUtils:
    """Test suite for utility functions."""
    
    def test_validate_audio_file_nonexistent(self):
        """Test validation of nonexistent file."""
        assert validate_audio_file("/nonexistent/file.wav") is False
        
    def test_validate_audio_file_valid_extensions(self):
        """Test validation of files with valid extensions."""
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_path = tmp.name
            
        try:
            assert validate_audio_file(tmp_path) is True
        finally:
            os.unlink(tmp_path)
            
    def test_validate_audio_file_invalid_extension(self):
        """Test validation of file with invalid extension."""
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
            tmp_path = tmp.name
            
        try:
            assert validate_audio_file(tmp_path) is False
        finally:
            os.unlink(tmp_path)
            
    def test_ensure_output_dir_creates_directory(self):
        """Test that ensure_output_dir creates directories."""
        with tempfile.TemporaryDirectory() as tmpdir:
            test_path = os.path.join(tmpdir, "subdir", "output.wav")
            ensure_output_dir(test_path)
            
            assert os.path.exists(os.path.dirname(test_path))
