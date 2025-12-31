# Examples Directory

This directory contains example scripts demonstrating how to use the `xtts_voice_clone` package.

## Available Examples

### basic_usage.py
Demonstrates the basic usage of the VoiceCloner class for generating a single voice clone from text.

**Usage:**
```bash
python examples/basic_usage.py
```

### batch_processing.py
Shows how to generate multiple voice clones from a list of texts using the same reference audio.

**Usage:**
```bash
python examples/batch_processing.py
```

## Requirements

Before running these examples, make sure you have:
1. Installed the package: `pip install -e .`
2. A reference audio file (2-5 minutes of clean speech)
3. Updated the `speaker_wav` path in the examples to point to your audio file

## Note

These examples are designed to work both locally (with GPU) and in Google Colab. Adjust file paths accordingly for your environment.
