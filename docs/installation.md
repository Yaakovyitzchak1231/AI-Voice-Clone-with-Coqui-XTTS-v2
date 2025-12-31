# Installation Guide

## Requirements

- Python 3.11 or higher
- CUDA-capable GPU (recommended) or CPU
- 4GB+ RAM for model loading

## Installation Methods

### Method 1: Install from Source (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/Yaakovyitzchak1231/AI-Voice-Clone-with-Coqui-XTTS-v2.git
cd AI-Voice-Clone-with-Coqui-XTTS-v2

# Install in editable mode with development dependencies
pip install -e ".[dev]"
```

### Method 2: Install Dependencies Only

```bash
pip install -r requirements.txt
```

### Method 3: Using Make (Unix/Linux/macOS)

```bash
# Install package dependencies
make install

# Or install with development tools
make install-dev
```

## PyTorch Installation

This project uses PyTorch 2.1.0 with CUDA 11.8 support. The installation is handled automatically by the requirements, but if you need to install it manually:

### For GPU (CUDA 11.8):
```bash
pip install torch==2.1.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cu118
```

### For CPU Only:
```bash
pip install torch==2.1.0 torchaudio==2.1.0 --index-url https://download.pytorch.org/whl/cpu
```

## Google Colab Setup

No installation is required for Google Colab! Just follow these steps:

1. Open the Colab notebook from the main README
2. Enable GPU: Runtime → Change runtime type → T4 GPU
3. Run the cells in order

The notebook will handle all installations automatically.

## Verification

Verify your installation by running:

```python
python -c "import torch; print(f'PyTorch version: {torch.__version__}'); print(f'CUDA available: {torch.cuda.is_available()}')"
```

Expected output:
```
PyTorch version: 2.1.0+cu118
CUDA available: True  # or False if running on CPU
```

## Troubleshooting

### Issue: CUDA not detected
- Ensure you have NVIDIA drivers installed
- Verify CUDA 11.8 is installed
- Try reinstalling PyTorch with the correct CUDA version

### Issue: Out of Memory
- Try using a smaller batch size
- Close other GPU-using applications
- Consider using CPU instead (slower but works)

### Issue: Import errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (should be 3.11+)

## Next Steps

After installation, check out the [Usage Guide](usage.md) to learn how to use the package.
