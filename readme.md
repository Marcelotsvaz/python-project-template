# 🐍 Python Project Template
Template to quickly bootstrap Python projects.

Uses [PDM](https://pdm.fming.dev/) to manage dependencies, build distributions and publish to package repositories.


## ✨ Features
- Centralized configuration in `pyproject.toml`
- Dependency management with [PDM](https://pdm.fming.dev/)
- Testing with [unittest](https://docs.python.org/3/library/unittest.html)
- Linting with [Pylint](https://github.com/pylint-dev/pylint)
- Integration with [Visual Studio Code](https://code.visualstudio.com/)
- Building and publishing to [PyPI](https://pypi.org/)
- Documentation hosted on [GitLab Pages](https://docs.gitlab.com/ee/user/project/pages/)
- CI/CD with [GitLab](https://docs.gitlab.com/ee/ci/)
- Several useful examples
	- Type hints
	- Logging
	- CLI

For a detailed description of all features check the [documentation](https://marcelotsvaz.gitlab.io/python-project-template/documentation/) and the [examples](examples/).


## Installation
Install from [PyPI](https://pypi.org/):
```sh
pip install marcelotsvaz-python-project-template
```

Install from wheel:
```sh
pip install marcelotsvaz_python_project_template-1.0.0-py3-none-any.whl
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
git tag 1.0.0
```

Build wheel with PDM:
```sh
pdm build
```

## Publish
Publish to PyPI:
```sh
pdm publish
```

Install the [keyring](https://pypi.org/project/keyring/) package to save PyPI credentials in the system keyring.


## Contributing
TODO: Contributing.