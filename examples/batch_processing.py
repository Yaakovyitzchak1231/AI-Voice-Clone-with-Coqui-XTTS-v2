"""
Example: Batch voice cloning

This example demonstrates how to generate multiple voice clones
from a list of texts using the same reference audio.
"""

from xtts_voice_clone import VoiceCloner
from xtts_voice_clone.utils import ensure_output_dir


def main():
    """
    Generate multiple voice clones from a list of texts.
    """
    # Initialize and load model
    print("Initializing VoiceCloner...")
    cloner = VoiceCloner()
    cloner.load_model()
    
    # Reference audio
    speaker_wav = "/content/drive/MyDrive/your_audio_sample.wav"
    
    # List of texts to generate
    texts = [
        "Welcome to the first chapter of our story.",
        "In the second chapter, things get more interesting.",
        "The third chapter brings unexpected twists.",
        "Finally, in the conclusion, everything comes together."
    ]
    
    # Generate each voice clone
    for i, text in enumerate(texts, 1):
        output_path = f"output/chapter_{i}.wav"
        ensure_output_dir(output_path)
        
        print(f"\nGenerating chapter {i}/{len(texts)}...")
        cloner.clone_voice(
            text=text,
            speaker_wav=speaker_wav,
            language="en",
            output_path=output_path
        )
        print(f"✓ Saved to {output_path}")
    
    print("\n✓ All chapters generated successfully!")


if __name__ == "__main__":
    main()
