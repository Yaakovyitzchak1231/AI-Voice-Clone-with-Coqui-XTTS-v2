# API Reference

## Module: `xtts_voice_clone`

The main module for voice cloning functionality.

### Class: `VoiceCloner`

Main class for performing voice cloning operations.

#### `__init__(device: Optional[str] = None)`

Initialize the VoiceCloner.

**Parameters:**
- `device` (str, optional): Device to run the model on. Options:
  - `"cuda"` - Use NVIDIA GPU
  - `"cpu"` - Use CPU
  - `None` - Auto-detect (uses CUDA if available, otherwise CPU)

**Example:**
```python
# Auto-detect device
cloner = VoiceCloner()

# Explicitly use GPU
cloner = VoiceCloner(device="cuda")

# Force CPU usage
cloner = VoiceCloner(device="cpu")
```

#### `load_model() -> VoiceCloner`

Load the XTTS-v2 model.

**Returns:**
- Self (for method chaining)

**Raises:**
- `RuntimeError`: If model fails to load

**Example:**
```python
cloner = VoiceCloner()
cloner.load_model()

# Or with method chaining
cloner = VoiceCloner().load_model()
```

#### `clone_voice(text: str, speaker_wav: str, language: str = "en", output_path: str = "cloned_voice.wav") -> str`

Generate voice clone from text using reference audio.

**Parameters:**
- `text` (str): Text to synthesize
- `speaker_wav` (str): Path to reference audio file (.wav, .mp3, .m4a, .flac)
- `language` (str, optional): Language code. Default: "en"
- `output_path` (str, optional): Path to save generated audio. Default: "cloned_voice.wav"

**Returns:**
- `str`: Path to the generated audio file

**Raises:**
- `RuntimeError`: If model is not loaded
- `FileNotFoundError`: If speaker_wav does not exist

**Example:**
```python
cloner = VoiceCloner().load_model()

output = cloner.clone_voice(
    text="Hello world!",
    speaker_wav="reference.wav",
    language="en",
    output_path="output.wav"
)
print(f"Generated: {output}")
```

## Module: `xtts_voice_clone.utils`

Utility functions for audio processing and file handling.

### `validate_audio_file(file_path: str) -> bool`

Validate if the audio file exists and has correct format.

**Parameters:**
- `file_path` (str): Path to audio file

**Returns:**
- `bool`: True if file is valid, False otherwise

**Example:**
```python
from xtts_voice_clone.utils import validate_audio_file

if validate_audio_file("audio.wav"):
    print("Valid audio file")
else:
    print("Invalid or missing audio file")
```

### `ensure_output_dir(output_path: str) -> None`

Ensure the output directory exists.

**Parameters:**
- `output_path` (str): Path to output file

**Example:**
```python
from xtts_voice_clone.utils import ensure_output_dir

ensure_output_dir("output/audio/file.wav")
# Creates 'output/audio/' if it doesn't exist
```

## Supported Languages

The XTTS-v2 model supports the following languages:

| Code | Language |
|------|----------|
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `de` | German |
| `it` | Italian |
| `pt` | Portuguese |
| `pl` | Polish |
| `tr` | Turkish |
| `ru` | Russian |
| `nl` | Dutch |
| `cs` | Czech |
| `ar` | Arabic |
| `zh-cn` | Chinese (Simplified) |
| `ja` | Japanese |
| `hu` | Hungarian |
| `ko` | Korean |

## Error Handling

Common exceptions and how to handle them:

### RuntimeError: "Model not loaded"

```python
try:
    cloner = VoiceCloner()
    cloner.clone_voice(...)  # Error: forgot to load model
except RuntimeError as e:
    print(f"Error: {e}")
    # Solution: Call load_model() first
    cloner.load_model()
```

### FileNotFoundError

```python
try:
    cloner.clone_voice(
        text="Test",
        speaker_wav="/nonexistent/file.wav"
    )
except FileNotFoundError:
    print("Reference audio file not found")
```

## Performance Considerations

### GPU vs CPU

- **GPU (CUDA)**: 5-10x faster, recommended for production
- **CPU**: Slower but works without GPU

### Memory Usage

- Model size: ~1.8GB
- Peak memory during inference: ~3-4GB
- Recommendation: 8GB+ RAM, 4GB+ VRAM for GPU

### Generation Speed

Approximate times (T4 GPU):
- Short text (10 words): ~2-3 seconds
- Medium text (50 words): ~5-8 seconds
- Long text (200 words): ~15-25 seconds

CPU is approximately 10x slower.
