# Installation
## 1. Git & Python
This project uses GitHub for version control and is written in Python. So first, ensure you have installed:
- [git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

## 2. pipx
[pipx](https://pypa.github.io/pipx/) is used to install some of the required libraries globally. Follow the system-specific instructions below to install it.

<details>
  <summary>Linux</summary>

  Launch Command Line and install pipx using the commands below.
  ```bash
  python3 -m pip install --user pipx
  python3 -m pipx ensurepath
  ```

</details>

<details>
  <summary>Mac</summary>

  Launch Terminal and install pipx using the commands below.
  ```bash
  brew install pipx
  pipx ensurepath
  ```

</details>

<details>
  <summary>Windows</summary>

  Launch Command Prompt and install pipx using the command below. **This assumes Python was not installed through the Microsoft Store - if it was, change ```py``` to ```python```.**
  ```bash
  py -m pip install --user pipx
  ```
  
  If you get a warning that says:
  ```bash
  WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
  ```
  Note the path and change to that directory:
  ```bash
  cd <USER folder>\AppData\Roaming\Python\Python3x\Scripts
  ```
  
  Then, run the following command. **Again, this assumes Python was not installed through the Microsoft Store - if it was, change ```py``` to ```python```.**
  ```bash
  py -m pipx ensurepath
  ```
  You will then need to relaunch the command prompt for the PATH variable changes to take effect.

</details>

## 3. Make (Windows Only)
This project makes use of Makefiles, which are run with the ```make``` command. This is available by default on Mac & Linux, but for windows you will need to install it.

<details>
  <summary>Installation Instructions</summary>

  First, ensure you have installed [chocolately](https://chocolatey.org/install). It can be installed by launching PowerShell **AS AN ADMINISTRATOR** and using the command:
   ```bash
  Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
  ```
  Then you can install make using:
  ```bash
  choco install make
  ```

</details>

## 4. PDM
This project uses [PDM](https://pdm-project.org/latest/) to manage the Python environment and support packaging. Follow the system-specific instructions below to install it.

<details>
  <summary>Linux</summary>

  Launch Command Line and install pdm using the command below.
  ```bash
  curl -sSL https://pdm-project.org/install-pdm.py | python3 -
  ```

</details>

<details>
  <summary>Mac</summary>

  Launch Terminal and install pdm using the command below.
  ```bash
  curl -sSL https://pdm-project.org/install-pdm.py | python3 -
  ```

</details>

<details>
  <summary>Windows</summary>

  Launch PowerShell and install pdm using the command below. **This assumes Python was not installed through the Microsoft Store - if it was, change ```py``` to ```python```.**
  ```bash
  (Invoke-WebRequest -Uri https://pdm-project.org/install-pdm.py -UseBasicParsing).Content | py -
  ```

</details>

## 5. VS Code (Optional)
If you're working in [VS Code](https://code.visualstudio.com/), .vscode settings files are provided.

TODO: more info on duty tasks, VS Code set up

# Development
## Cloning the Repository

## Setting up the Environment

## Pre-commit

## Commit Message Convention

TODO:
    - when to install pre-commit
    - have pre-commit autoinstall
    - have pre-commit run duty tasks? keeps consitency with actions
    - pre-commit angular commit convention
