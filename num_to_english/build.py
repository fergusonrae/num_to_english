import os
import pathlib
from pynt import task

PROJECT_NAME = "num_to_english"
DEV_SETTINGS = f"{PROJECT_NAME}.settings.development"
PROD_SETTINGS = f"{PROJECT_NAME}.settings.production"


@task()
def build():
    """Install dependencies"""
    os.chdir(get_root_path())
    docker_build_command = [
        "docker", "build",
        "-t", PROJECT_NAME,
        "."
    ]
    run_command(" ".join(docker_build_command))


@task()
def run_dev():
    """Run development server"""
    run_common(DEV_SETTINGS)


@task()
def run_prod():
    """Run production server"""
    run_common(PROD_SETTINGS)


@task()
def test():
    """Run tests"""
    # docker run --rm -it -v $(PWD):/app -w /app $(PROJECT_NAME) python manage.py test
    pass


def run_command(command):
    exit_code = os.system(command)
    if exit_code != 0:
        raise Exception(f"Command {command} failed with exit code {exit_code}")


def get_root_path():
    # TODO: maybe can be fancier?
    return pathlib.Path(__file__).parent.parent.resolve()


def run_common(settings):
    docker_run_command = [
        "docker run --rm",
        f"-e DJANGO_SETTINGS_MODULE={settings}",
        "-p 8000:8000",
        PROJECT_NAME,
        f"python manage.py runserver 0.0.0.0:8000",
    ]
    run_command(" ".join(docker_run_command))
