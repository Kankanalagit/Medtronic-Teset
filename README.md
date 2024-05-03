# Introduction

This is a base level project to test open source API https://swapi.dev/ functional test automation with Python & Pytest framework with allure reporting.

For further information on pytest, take a look at https://docs.pytest.org/en/stable/


# Project Setup

This project is build with `python 3.12`

It is recommended to use a python virtual environment to run python projects. You can set it up by following this: https://github.com/pyenv/pyenv-virtualenv

Once your python environment is setup, you need to install the required packages by running

```
pip install pytest
pip install allure
pip install requests
```

## Tests package
To run functional tests run

```
pytest
```

This runs all the test files configured in `pytest.ini`

The run also generates result artifacts under the `results` directory. These results can be viewed as an HTML page by running

To run specific test
```
pytest -k "test_name"
```

To run group of tests marked using markers
```
pytest -m "smoke or regression"
```

## Framework Organization

```
├── README.md
├── actions
│   ├── base_actions.py     - Base API actions for all other actions file
│   └── get_actions.py     - API actions related to people feature
├── utils
│   ├── config.py          -environment setup
├── tests
│   ├── test_people.py  -  functional test file for people attribute
│   ── baseclass.py  -  reusable methods and test data
├── testdata        - testdata placeholder
├── results                 - results directory
└── pytest.ini               - Pytest config
```

#Medtronic
