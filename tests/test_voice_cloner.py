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
            
    @patch('xtts_voice_clone.voice_cloner.TTS')
    def test_clone_voice_with_model(self, mock_tts):
        """Test voice cloning with loaded model."""
        mock_tts_instance = Mock()
        mock_tts.return_value = mock_tts_instance
        mock_tts_instance.to.return_value = mock_tts_instance
        
        cloner = VoiceCloner()
        cloner.load_model()
        
        result = cloner.clone_voice(
            text="Test text",
            speaker_wav="/path/to/audio.wav",
            language="en",
            output_path="output.wav"
        )
        
        assert result == "output.wav"
        mock_tts_instance.tts_to_file.assert_called_once()
