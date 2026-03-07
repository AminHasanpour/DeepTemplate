> Guidance for autonomous coding agents
> Read this before writing, editing, or executing anything in this repo.

# Relevant commands

* The project uses `pip` for management of packages. This means:
  * To install packages, use `pip install <package-name>`.
  * To run Python scripts, use `python <script-name>.py`.
  * To run other commands related to Python, use `python <command>`.
* The project uses `pytest` for testing. To run tests, use `pytest tests/`.
* The project uses `ruff` for linting and formatting:
    * To format code, use `ruff format .`.
    * To lint code, use `ruff check . --fix`.
* The project uses `invoke` for task management. To see available tasks, refer to the `tasks.py` file.
* The project uses `pre-commit` for managing pre-commit hooks. To run all hooks on all files, use
    `pre-commit run --all-files`. For more information, refer to the `.pre-commit-config.yaml` file.

# Coding standards

* Follow existing code style and conventions in the project.
* Refer to [agents/coding_standards.md](agents/coding_standards.md) for detailed coding standards and best practices.

# Testing guidelines

* Refer to [agents/testing_guidelines.md](agents/testing_guidelines.md) for detailed testing guidelines and best practices.
