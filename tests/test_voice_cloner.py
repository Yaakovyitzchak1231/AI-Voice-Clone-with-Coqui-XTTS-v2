"""
Unit tests for the VoiceCloner class.
"""

import pytest
import torch
from unittest.mock import Mock, patch, MagicMock
from xtts_voice_clone import VoiceCloner


class TestVoiceCloner:
    """Test suite for VoiceCloner class."""
    
    def test_initialization_default_device(self):
        """Test VoiceCloner initializes with correct default device."""
        cloner = VoiceCloner()
        expected_device = "cuda" if torch.cuda.is_available() else "cpu"
        assert cloner.device == expected_device
        
    def test_initialization_custom_device(self):
        """Test VoiceCloner initializes with custom device."""
        cloner = VoiceCloner(device="cpu")
        assert cloner.device == "cpu"
        
    @patch('xtts_voice_clone.voice_cloner.TTS')
    def test_load_model(self, mock_tts):
        """Test model loading."""
        mock_tts_instance = Mock()
        mock_tts.return_value = mock_tts_instance
        mock_tts_instance.to.return_value = mock_tts_instance
        
        cloner = VoiceCloner()
        result = cloner.load_model()
        
        assert result == cloner  # Check method chaining
        assert cloner.tts is not None
        mock_tts.assert_called_once()
        
    def test_clone_voice_without_model(self):
        """Test that clone_voice raises error when model not loaded."""
        cloner = VoiceCloner()
        
        with pytest.raises(RuntimeError, match="Model not loaded"):
            cloner.clone_voice(
                text="Test text",
                speaker_wav="/path/to/audio.wav"
            )
    
    @patch('xtts_voice_clone.voice_cloner.ensure_output_dir')
    @patch('xtts_voice_clone.voice_cloner.validate_audio_file')
    @patch('xtts_voice_clone.voice_cloner.TTS')
    def test_clone_voice_with_model(self, mock_tts, mock_validate, mock_ensure_dir):
        """Test voice cloning with loaded model."""
        mock_tts_instance = Mock()
        mock_tts.return_value = mock_tts_instance
        mock_tts_instance.to.return_value = mock_tts_instance
        mock_validate.return_value = True
        
        cloner = VoiceCloner()
        cloner.load_model()
        
        result = cloner.clone_voice(
            text="Test text",
            speaker_wav="/path/to/audio.wav",
            language="en",
            output_path="output.wav"
        )
        
        assert result == "output.wav"
        mock_validate.assert_called_once_with("/path/to/audio.wav")
        mock_ensure_dir.assert_called_once_with("output.wav")
        mock_tts_instance.tts_to_file.assert_called_once()
    
    @patch('xtts_voice_clone.voice_cloner.validate_audio_file')
    @patch('xtts_voice_clone.voice_cloner.TTS')
    def test_clone_voice_invalid_audio(self, mock_tts, mock_validate):
        """Test that clone_voice raises error for invalid audio file."""
        mock_tts_instance = Mock()
        mock_tts.return_value = mock_tts_instance
        mock_tts_instance.to.return_value = mock_tts_instance
        mock_validate.return_value = False
        
        cloner = VoiceCloner()
        cloner.load_model()
        
        with pytest.raises((FileNotFoundError, ValueError)):
            cloner.clone_voice(
                text="Test text",
                speaker_wav="/nonexistent/audio.wav"
            )
