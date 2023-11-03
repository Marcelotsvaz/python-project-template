## Build and Release
For a release, create a git tag first:
``` sh
git tag 1.0.0
```

Build wheel with PDM:
``` sh
pdm build
```

## Publish
Publish to PyPI:
``` sh
pdm publish
```

Install the [keyring](https://pypi.org/project/keyring/) package to save PyPI credentials in the system keyring.