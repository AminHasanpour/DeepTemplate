import os

from invoke import Context, task

WINDOWS = os.name == "nt"
PROJECT_NAME = "{{ cookiecutter.project_name }}"
PYTHON_VERSION = "{{ cookiecutter.python_version }}"

# Project commands
@task
def test(ctx: Context) -> None:
    """Run tests."""
    ctx.run("uv run coverage run -m pytest tests/", echo=True, pty=not WINDOWS)
    ctx.run("uv run coverage report -m -i", echo=True, pty=not WINDOWS)

# Documentation commands
@task
def build_docs(ctx: Context) -> None:
    """Build documentation."""
    ctx.run("uv run zensical build --config-file docs/mkdocs.yaml --site-dir build", echo=True, pty=not WINDOWS)

@task
def serve_docs(ctx: Context) -> None:
    """Serve documentation."""
    ctx.run("uv run zensical serve --config-file docs/mkdocs.yaml", echo=True, pty=not WINDOWS)
