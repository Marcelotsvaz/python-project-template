# Python Project Template
Template for a Python application/library project.


## Features
- Manage dependencies with [PDM](https://pdm.fming.dev/).
- Stores metadata, build and tools configuration in `pyproject.toml`.
- CLI with `argparse`.
- Type annotations.

<!-- [PEP 518](https://peps.python.org/pep-0518/ 'PEP 518 - Specifying Minimum Build System Requirements for Python Projects') and [PEP 621](https://peps.python.org/pep-0621/ 'PEP 621 - Storing project metadata in pyproject.toml'). -->


## Installation
Install from [PyPI](https://pypi.org/):
```sh
pip install python-template
```

Install from wheel:
```sh
pip install python_template-1.0.0-py3-none-any.whl
```


## Development
Create virtual environment:
```sh
python -m venv --upgrade-deps .venv
source .venv/bin/activate
```

Install project in editable mode with development dependencies:
```sh
pdm install --dev
```


## Debugging
TODO: Debugging with VS Code.


## Unit Tests and Code Coverage
Run tests and print coverage report with PDM script:
```sh
pdm test
```

Above command is equivalent to:
```sh
coverage run -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose && coverage report
```

Show all scripts:
```sh
pdm run --list
```


## Manage Dependencies
Add dependencies with PDM:
```sh
pdm add django
pdm add --group json jsons	# Optional dependency.
pdm add --dev pylint	# Development dependency.
```

Resulting changes in `pyproject.toml`:
```toml
[project]
	dependencies = [
		'django >= 4.2.5',
	]
	
	optional-dependencies.json = [
		'jsons >= 1.6.3',
	]


[tool.pdm]
	dev-dependencies.dev = [
		'pylint >= 2.17.5',
	]
```


## Build and Release
For a release, create a git tag first:
```sh
git tag 1.1.0
```

Build wheel with PDM:
```sh
pdm build
```


## Contributing
TODO: Contributing.