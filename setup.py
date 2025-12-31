from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ai-voice-clone-xtts-v2",
    version="1.0.0",
    author="Robert Hall",
    description="Free voice cloning for creators using Coqui XTTS-v2 on Google Colab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yaakovyitzchak1231/AI-Voice-Clone-with-Coqui-XTTS-v2",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.11",
    install_requires=[
        "TTS>=0.20.0",
        "torch==2.1.0",
        "torchaudio==2.1.0",
        "transformers<4.50.0",
        "numpy>=1.24.0",
        "scipy>=1.10.0",
        "librosa>=0.10.0",
        "soundfile>=0.12.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
)
