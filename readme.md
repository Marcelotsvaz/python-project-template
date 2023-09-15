# Python Project Template
Template for a Python application/library project.


# Features
- Type hints
- CLI with `argparse`
- Examples
- Unit tests
- Code coverage
- Uses pyproject.toml
- Development dependencies
- Debugging


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
coverage run -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose && coverage report
```