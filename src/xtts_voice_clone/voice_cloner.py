"""
Voice cloning module using Coqui XTTS-v2
"""

import os
import torch
from typing import Optional
from TTS.api import TTS


class VoiceCloner:
    """
    A wrapper class for voice cloning using Coqui XTTS-v2 model.
    
    This class provides a simple interface for loading the XTTS-v2 model
    and generating voice clones from text and reference audio.
    """
    
    def __init__(self, device: Optional[str] = None):
        """
        Initialize the VoiceCloner.
        
        Args:
            device: Device to run the model on ('cuda' or 'cpu'). 
                   If None, automatically detects available device.
        """
        os.environ['MPLBACKEND'] = 'Agg'
        
        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device
            
        self.tts = None
        
    def load_model(self):
        """
        Load the XTTS-v2 model.
        
        Returns:
            Self for method chaining.
        """
        self.tts = TTS('tts_models/multilingual/multi-dataset/xtts_v2').to(self.device)
        print(f'Model loaded on {self.device}!')
        return self
        
    def clone_voice(
        self,
        text: str,
        speaker_wav: str,
        language: str = "en",
        output_path: str = "cloned_voice.wav"
    ):
        """
        Generate voice clone from text using reference audio.
        
        Args:
            text: Text to synthesize.
            speaker_wav: Path to reference audio file.
            language: Language code (default: "en").
            output_path: Path to save the generated audio.
            
        Returns:
            Path to the generated audio file.
        """
        if self.tts is None:
            raise RuntimeError("Model not loaded. Call load_model() first.")
            
        self.tts.tts_to_file(
            text=text,
            speaker_wav=speaker_wav,
            language=language,
            file_path=output_path
        )
        
        print(f"Voice generated: {output_path}")
        return output_path
