# TKP Quiz
> Tran Ky Phong HighSchool Quiz

<br>

# Developed by
- Program language: `Python3 latest release`
- Framework: `Django latest version`
- Database: `Sqlite3`

<br>

# Installation Python3 and Setup Virtual Environment
## Windows OS
### Download and install Python3
- Visit [Python Official Website](https://www.python.org/) and download the latest version.

    > [!NOTE]
    > Remember tick on [Add Python 3.x to PATH](https://docs.blender.org/manual/vi/latest/_images/about_contribute_install_windows_installer.png) <br>
    > In windows 10 and later, you can install [Python in Microsoft Store](https://apps.microsoft.com/search?query=python)


### Create virtual environment
- Open this project

- Run this command to create a virtual environment
    ```bash
    python -m venv .venv
    ```

    > [!WARNING]
    > In windows 8.1/ 10/ 11 and later. You must allow run virtual environment. <br>
    > Open `powershell as administrator` and run this command
    ```bash
    Set-ExecutionPolicy Unrestricted -Force
    ```

- Run this command to active virtual environment
    ```bash
    .\.venv\Scripts\activate
    ```

    > [!NOTE]
    > You can create and manage virtual environment in [VSCode](https://code.visualstudio.com/docs/python/environments) or [Pycharm](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html)


## Ubuntu and Mac OS
### Download and install Python3
- Update your system's repository list by entering the following command
    ```bash
    sudo apt update
    ```

- Download the latest version of Python with
    ```bash
    sudo apt install python3
    ```

- Use the following command to install pip for Python 3
    ```bash
    sudo apt install python3-pip
    ```

### Create virtual environment
- Open this project

- Run this command to create a virtual environment
    ```bash
    python3 -m venv .venv
    ```

- Run this command to active virtual environment
    ```bash
    source .venv/bin/activate
    ```

<br>

# Setup project environment variables file
- Open this project

- Copy environment file
    ```bash
    cp .env.example .env
    ```

- Then edit some configuration settings for Project

<br>

# Build and start server
## Using Docker
### Download and install Docker-compose
#### Windows and Mac OS
- Visit [Docker Official Website](https://www.docker.com/) and download and install latest version

#### Ubuntu OS
- Follow the [documentation to install docker-compose in docker official website](https://docs.docker.com/engine/install/ubuntu/)

- Uninstall old versions
    ```bash
    for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do sudo apt-get remove $pkg; done
    ```

- Install using the apt repository
    - Add Docker's official GPG key:
        ```bash
        sudo apt-get update
        sudo apt-get install ca-certificates curl gnupg
        sudo install -m 0755 -d /etc/apt/keyrings
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
        sudo chmod a+r /etc/apt/keyrings/docker.gpg
        ```

    - Add the repository to Apt sources:
        ```bash
        echo \
        "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
        "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
        sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        ```

    - Update your system's repository list by entering the following command
        ```bash
        sudo apt update
        ```

- Install the Docker packages.
    ```bash
    sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    ```


### Build and start docker-compose
- Create bridge network
    ```bash
    docker network create [COMPOSE_PROJECT_NAME]_network
    ```
    > - `COMPOSE_PROJECT_NAME` is the project name setup in .env file

- Build docker-compose
    ```bash
    docker-compose build
    ```

- Up docker-compose
    ```bash
    docker-compose up
    ```
    > [!NOTE]
    > Using `-d` option for run docker-compose in the background <br>
    > Using `--build` option for build and up docker-compose

- Down docker-compose
    ```bash
    docker-compose down
    ```


## Using Python
- Run this command to install all python packages
    ```bash
    pip install -r requirements.txt
    ```

- Change directory to source code folder
    ```bash
    cd src/
    ```

- Migrate database
    ```bash
    python manage.py migrate
    ```

- Run server
    ```bash
    python manage.py runserver <HOST>:<PORT>
    ```
    > - HOST: `127.0.0.1` (loopback address) or `0.0.0.0` (non-routable meta-address)
    > - PORT: `80` (default HTTP) <br>
    > - If run on production. You must turn off `DEBUG`. And now you can use `Nginx` for return static file. If not available, you must add flag `--insecure`

<br>
