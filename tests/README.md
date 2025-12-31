# Tests Directory

This directory contains the test suite for the `xtts_voice_clone` package.

## Running Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_voice_cloner.py -v
```

### Run with coverage
```bash
pytest tests/ -v --cov=src/xtts_voice_clone --cov-report=term --cov-report=html
```

### Using Make
```bash
make test
```

## Test Files

- `conftest.py` - Test configuration and fixtures
- `test_voice_cloner.py` - Tests for the VoiceCloner class
- `test_utils.py` - Tests for utility functions

## Writing Tests

Follow these conventions when adding new tests:

1. Test files should be named `test_*.py`
2. Test classes should be named `Test*`
3. Test functions should be named `test_*`
4. Use descriptive test names that explain what is being tested
5. Use fixtures from `conftest.py` for common setup
6. Mock external dependencies (like TTS model loading)

## Test Coverage

Aim for high test coverage (>80%) for all new code. Check coverage with:

```bash
pytest tests/ --cov=src/xtts_voice_clone --cov-report=term-missing
```

## Continuous Integration

Tests are automatically run on push and pull requests via GitHub Actions. See `.github/workflows/ci.yml` for the CI configuration.
