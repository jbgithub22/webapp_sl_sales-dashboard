# 🐍 Poetry Cheatsheet: Essential Commands

Poetry is a dependency management and packaging tool for Python. It helps you declare the libraries your project depends on and it manages your virtual environments.

## 🚀 Project Setup and Initialization

| Command | Description |
| :--- | :--- |
| `poetry new my-project` | Creates a **new Python project** named `my-project` with a standard structure. |
| `poetry init` | **Initializes Poetry** in an existing project directory. It interactively asks for project details and creates a `pyproject.toml` file. |

***

## ⚙️ Environment and Dependencies

### Environment Management

| Command | Description |
| :--- | :--- |
| `poetry install` | **Installs all dependencies** listed in `pyproject.toml` and creates a **virtual environment** if one doesn't exist. This is the main command for setup. |
| `poetry shell` | **Spawns a new shell** within the project's virtual environment. Use this to activate the environment. |
| `exit` | **Exits** the Poetry virtual environment shell (standard shell command). |
| `poetry run <command>` | **Executes a command** within the project's virtual environment **without** explicitly activating the shell first. E.g., `poetry run python app.py`. |
| `poetry env list` | **Lists** all virtual environments associated with the project. |
| `poetry env remove <env_name>` | **Removes a specific** virtual environment. |

### Dependency Management

| Command | Description |
| :--- | :--- |
| `poetry add <package>` | **Adds a new package** to the main dependencies and installs it. E.g., `poetry add requests`. |
| `poetry add --dev <package>` | **Adds a package** specifically to the **development dependencies** (for testing, linting, etc.). E.g., `poetry add --dev pytest`. |
| `poetry remove <package>` | **Removes a package** from both the dependencies and the virtual environment. |
| `poetry update` | **Updates all dependencies** to the latest versions permitted by the constraints in `pyproject.toml` and updates `poetry.lock`. |
| `poetry show` | **Lists all installed** packages (dependencies). Use `poetry show --tree` for a tree view. |
| `poetry lock` | **Generates a `poetry.lock` file** without installing anything. This is useful for locking versions after manual changes to `pyproject.toml`. |

***

## 📦 Building and Publishing

| Command | Description |
| :--- | :--- |
| `poetry build` | **Builds the project's distributable archives** (source archive and wheel) in the `dist/` directory. |
| `poetry publish` | **Publishes** the built package to a repository (e.g., PyPI). Requires configuration. |
| `poetry check` | **Checks** the validity of the `pyproject.toml` file. |