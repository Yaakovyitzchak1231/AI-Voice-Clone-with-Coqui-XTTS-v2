# Usage Guide

## Quick Start

### Python Package Usage

```python
from xtts_voice_clone import VoiceCloner

# Initialize the voice cloner
cloner = VoiceCloner()

# Load the model (this downloads the model on first run)
cloner.load_model()

# Generate voice clone
cloner.clone_voice(
    text="Hello! This is a test of voice cloning.",
    speaker_wav="path/to/your/reference_audio.wav",
    language="en",
    output_path="output.wav"
)
```

### Google Colab Usage

See the main [README.md](../README.md) for detailed Colab instructions.

## Advanced Usage

### Batch Processing

Process multiple texts with the same voice:

```python
from xtts_voice_clone import VoiceCloner

cloner = VoiceCloner()
cloner.load_model()

texts = [
    "First sentence to generate.",
    "Second sentence to generate.",
    "Third sentence to generate."
]

for i, text in enumerate(texts):
    cloner.clone_voice(
        text=text,
        speaker_wav="reference.wav",
        language="en",
        output_path=f"output_{i}.wav"
    )
```

### Using Different Languages

XTTS-v2 supports multiple languages:

```python
# Spanish
cloner.clone_voice(
    text="Hola, ¿cómo estás?",
    speaker_wav="reference.wav",
    language="es",
    output_path="spanish_output.wav"
)

# French
cloner.clone_voice(
    text="Bonjour, comment allez-vous?",
    speaker_wav="reference.wav",
    language="fr",
    output_path="french_output.wav"
)
```

Supported language codes:
- `en` - English
- `es` - Spanish
- `fr` - French
- `de` - German
- `it` - Italian
- `pt` - Portuguese
- `pl` - Polish
- `tr` - Turkish
- `ru` - Russian
- `nl` - Dutch
- `cs` - Czech
- `ar` - Arabic
- `zh-cn` - Chinese (Simplified)
- `ja` - Japanese
- `hu` - Hungarian
- `ko` - Korean

### Device Selection

Explicitly choose CPU or GPU:

```python
# Use GPU if available
cloner = VoiceCloner(device="cuda")

# Force CPU usage
cloner = VoiceCloner(device="cpu")

# Auto-detect (default)
cloner = VoiceCloner()  # Uses CUDA if available, otherwise CPU
```

## Best Practices

### Reference Audio

For best results, your reference audio should:

- Be 2-5 minutes long
- Have clear speech with minimal background noise
- Include varied intonations and speaking styles
- Be in the same language as the target text
- Have consistent audio quality throughout

### Text Input

- Keep sentences reasonably short (< 200 words)
- Use proper punctuation for natural pauses
- Avoid special characters or formatting
- Match the language of your reference audio

### Output Quality

Factors affecting output quality:

1. **Reference audio quality** - Most important factor
2. **Text complexity** - Simpler sentences work better
3. **Language matching** - Use same language as reference
4. **Hardware** - GPU provides better/faster results

## Examples

See the [examples/](../examples/) directory for complete working examples:

- `basic_usage.py` - Simple voice cloning
- `batch_processing.py` - Processing multiple texts

## Troubleshooting

### Poor Audio Quality

- Use higher quality reference audio
- Try a longer reference audio sample (3-5 minutes)
- Ensure reference audio is clean (no background noise)
- Check that language codes match

### Slow Generation

- Use GPU instead of CPU
- Close other GPU-using applications
- Use Google Colab for free GPU access

### Memory Errors

- Reduce text length
- Use CPU mode instead of GPU
- Close other applications
- Restart your Python session

## API Reference

### VoiceCloner Class

```python
class VoiceCloner:
    def __init__(self, device: Optional[str] = None)
    def load_model(self) -> VoiceCloner
    def clone_voice(
        self,
        text: str,
        speaker_wav: str,
        language: str = "en",
        output_path: str = "cloned_voice.wav"
    ) -> str
```

For more details, see the source code documentation.
