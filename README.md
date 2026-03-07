# 🍪 A Cookiecutter template for Deep Learning projects

Inspired by the original [DTU's MLOps template](https://github.com/SkafteNicki/mlops_template), this template has been updated to better fit deep learning projects.

## ✋ Requirements to use the template:

* Python 3.11 or higher
* [cookiecutter](https://github.com/cookiecutter/cookiecutter) version 2.4.0 or higher

## 🆕 Start a new project

On your local machine run

```bash
cookiecutter https://github.com/AminHasanpour/DeepTemplate.git
```

You will be prompted with the following questions:

```txt
    [1/8] repo_name (repo_name):
    [2/8] project_name (project_name):
    [3/8] Select project_structure
        1 - advance
        2 - simple
        Choose from [1/2] (1):
    [4/8] Select deps_manager
        1 - pip
        2 - uv
        Choose from [1/2] (1):
    [5/8] author_name (Your name (or your organization/company/team)):
    [6/8] description (A short description of the project.):
    [7/8] python_version (3.12):
    [8/8] Select open_source_license
        1 - No license file
        2 - MIT
        3 - BSD-3-Clause
        Choose from [1/2/3] (1):
```

Where you should input starting values for the project. A couple of notes regarding the different options:

1. When asked for the `repo_name` e.g. the repository name, this should be the same as when you created the Github
    repository in the beginning.

2. When asked for the `project_name` this should be a
    [valid Python package name](https://peps.python.org/pep-0008/#package-and-module-names). This means that the name
    should be all lowercase and only contain letters, numbers and underscores. The project name will be used as the name
    of the Python package. This will automatically be validated by the template.

3. When asked for the `project_structure` you can choose between `advance` and `simple`. The `advance` structure
    contains everything in the `simple` structure but also includes starting `dockerfiles`, `docs`, `github actions`,
    `dependabot` and more.

## 🗃️ Repository structure

Assuming you choose the `advance` structure and `uv` as the dependency manager, the repository will look like
something like this:

```txt
├── configs
│   └── .gitkeep
├── .devcontainer
│   ├── devcontainer.json
│   └── postCreateCommand.sh
├── dockerfiles
│   └── .gitkeep
├── docs
│   ├── mkdocs.yaml
│   ├── README.md
│   └── source
│       └── index.md
├── .github
│   ├── dependabot.yaml
│   └── workflows
│       ├── linting.yaml
│       ├── pre-commit-update.yaml
│       └── tests.yaml
├── .gitignore
├── LICENSE
├── models
│   └── .gitkeep
├── .pre-commit-config.yaml
├── pyproject.toml
├── .python-version
├── README.md
├── src
│   └── project_name
│       └── __init__.py
├── tasks.py
├── tests
│   └── .gitkeep
└── uv.lock
```

## 📚 The stack

🐍 Python projects using `pyproject.toml`

🔥 Models in [Pytorch](https://pytorch.org/)

📦 Containerized using [Docker](https://www.docker.com/)

📄 Documentation with [Material Mkdocs](https://squidfunk.github.io/mkdocs-material/)

👕 Linting and formatting with [ruff](https://docs.astral.sh/ruff/)

✅ Checking using [pre-commit](https://pre-commit.com/)

🛠️ CI with [GitHub Actions](https://github.com/features/actions)

🤖 Automated dependency updates with [Dependabot](https://github.com/dependabot)

📝 Project tasks using [Invoke](https://www.pyinvoke.org/)

and probably more that I have forgotten...

## ❕ License

If you enjoy using the template, please consider giving credit by citing it.
You can use the following BibTeX entry:

```bibtex
@misc{skafte_mlops_template,
    author       = {Nicki Skafte Detlefsen},
    title        = {MLOps template},
    howpublished = {\url{https://github.com/SkafteNicki/mlops_template}},
    year         = {2025}
}
```
