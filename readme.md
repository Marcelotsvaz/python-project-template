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


## 📂 Project Structure
```
📂 Python Project Template
├─ 📁 .staging				Build artifacts and other ignored files
├─ 📁 .vscode				VS Code configuration
├─ 📁 build					Build scripts and local PDM plugins
├─ 📂 doc					Documentation
│  ├─ 📁 documentation		Sources for TODO documentation
│  └─ 📁 homepage			Project homepage on GitLab Pages
├─ 📁 examples				Examples
├─ 📁 project_template		Main package
├─ 📁 tests					Tests for the main package
├─ 🔶 .gitignore			Git ignored files
├─ 🦊 .gitlab-ci.yml		GitLab CI/CD configuration
├─ 🔒 pdm.lock				Dependency lock file
├─ ⚙️ pyproject.toml		Project metadata and tool configuration
├─ 📄 readme.md				Readme (this file)
└─ 📜 unlicense.txt			License
```


## Contributing
TODO: Contributing.