import os
import sys
import venv
import subprocess
from pathlib import Path


def main():

    venv_dir = Path(".venv")
    requirements_file = Path("requirements.txt")

    if not venv_dir.exists():
        print("Creating virtual environment...")
        venv.create(venv_dir, with_pip=True)
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")

    if os.name == "nt":
        venv_python = venv_dir / "Scripts" / "python.exe"
        venv_pip = venv_dir / "Scripts" / "pip.exe"
    else:
        venv_python = venv_dir / "bin" / "python"
        venv_pip = venv_dir / "bin" / "pip"

    if not venv_python.exists():
        print(f"Error: Python executable not found at {venv_python}")
        sys.exit(1)

    if requirements_file.exists():
        print("Installing dependencies from requirements.txt...")
        run_command([str(venv_pip), "install", "-r", "requirements.txt"])
        print("Dependencies installed.")
    else:
        print("No requirements.txt found. Skipping dependency installation.")

    run_command([venv_python, "manage.py", "makemigrations"])
    run_command([venv_python, "manage.py", "migrate"])
    try:
        run_command([venv_python, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
        sys.exit(0)


def run_command(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command '{' '.join(command)}' failed with error: {e}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
