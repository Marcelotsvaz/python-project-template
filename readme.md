# Python Project Template
Template for a Python application/library project.



# Features
TODO


## Setup in Virtual Environment
```sh
# Create virtual environment.
python -m venv --upgrade-deps .venv

# Install project in editable mode with development dependencies.
pip install -e .[dev]
```

```sh
pdm add django
pdm add --group json jsons
pdm add --dev pylint
pdm install
pdm build
```


## Uses pyproject.toml
Uses [PEP 518](https://peps.python.org/pep-0518/ 'PEP 518 - Specifying Minimum Build System Requirements for Python Projects') and [PEP 621](https://peps.python.org/pep-0621/ 'PEP 621 - Storing project metadata in pyproject.toml').


## Type Hints
TODO


## CLI With `argparse`
TODO


## Examples
TODO


## Development Dependencies
```toml
# pyproject.toml
[project]
	optional-dependencies.dev = [
		'pylint >= 2.17.5',
	]
```

```sh
# Install project in editable mode with development dependencies.
pip install -e .[dev]
```


## Debugging
TODO Debugging with VS Code.


## Unit Tests and Code Coverage
```sh
# Run tests with coverage report.
pdm test

# Run directly.
coverage run -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose && coverage report

# Run directly without code coverage.
python -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose
```



# Contributing
TODO