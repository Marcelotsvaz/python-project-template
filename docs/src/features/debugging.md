## Debugging
TODO: Debugging with VS Code.


## Unit Tests and Code Coverage
Run tests and print coverage report with PDM script:
``` sh
pdm run test
```

Above command is equivalent to:
``` sh
coverage run -m unittest discover --pattern '*_tests.py' --start-directory tests/ --verbose && coverage report
```

Show all scripts:
``` sh
pdm run --list
```