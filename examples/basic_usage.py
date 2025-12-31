"""
Example: Basic voice cloning usage

This example demonstrates the basic usage of the VoiceCloner class
for generating voice clones from text.
"""

from xtts_voice_clone import VoiceCloner


def main():
    """
    Basic example of voice cloning.
    
    Note: This example assumes you're running on a system with the model
    downloaded and a reference audio file available.
    """
    # Initialize the voice cloner
    print("Initializing VoiceCloner...")
    cloner = VoiceCloner()
    
    # Load the model
    print("Loading XTTS-v2 model...")
    cloner.load_model()
    
    # Text to synthesize
    text = "Hello! This is an example of AI voice cloning using Coqui XTTS-v2."
    
    # Path to your reference audio (replace with your actual file)
    speaker_wav = "/content/drive/MyDrive/your_audio_sample.wav"
    
    # Generate the cloned voice
    print("Generating voice clone...")
    output_path = cloner.clone_voice(
        text=text,
        speaker_wav=speaker_wav,
        language="en",
        output_path="output/cloned_voice.wav"
    )
    
    print(f"✓ Voice cloning complete! Output saved to: {output_path}")


if __name__ == "__main__":
    main()
