````markdown
# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project structure

The directory structure of the project looks like this:
```txt
├── .github/                  # Github actions and dependabot
│   ├── dependabot.yaml
│   └── workflows/
│       └── tests.yaml
├── configs/                  # Configuration files
├── dockerfiles/              # Dockerfiles
├── docs/                     # Documentation
│   ├── mkdocs.yml
│   └── source/
│       └── index.md
├── models/                   # Trained models
├── {{cookiecutter.project_name}}/             # Source code
│   └── __init__.py
└── tests/                    # Tests
├── .gitignore
├── .pre-commit-config.yaml
├── LICENSE
├── pyproject.toml            # Python project file
├── README.md                 # Project README
└── tasks.py                  # Project tasks
```


Created using [DeepTemplate](https://github.com/AminHasanpour/DeepTemplate),
a [cookiecutter template](https://github.com/cookiecutter/cookiecutter) for getting
started with Deep Learning Projects.

````
