# Installation

Install from [PyPI](https://pypi.org/):
``` sh
pip install marcelotsvaz-python-project-template
```

Install from wheel:
``` sh
pip install marcelotsvaz_python_project_template-1.0.0-py3-none-any.whl
```


## Manage Dependencies
Add dependencies with PDM:
``` sh
pdm add django
pdm add --group json jsons	# Optional dependency.
pdm add --dev pylint	# Development dependency.
```

Resulting changes in `pyproject.toml`:
``` toml
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

# Libraries vs Applications

optional-dependencies.json = [
	'jsons >= 1.6.3',
]