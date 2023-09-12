# Python Project Template
Template for a Python application/library project.


# Features
- Type hints
- CLI with `argparse`
- Unit tests
- Uses pyproject.toml
- Development dependencies


# Setup
```sh
# Create virtual environment.
python -m venv .venv

# Install project in editable mode with development dependencies.
pip install -e .[dev]
```


# Running Tests
```sh
# Run tests.
python -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose
```