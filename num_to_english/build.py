import os
import pathlib
from pynt import task

PROJECT_NAME = "num_to_english"
DEV_SETTINGS = f"{PROJECT_NAME}.settings.development"
PROD_SETTINGS = f"{PROJECT_NAME}.settings.production"


@task()
def generate_secret_key():
    """Generate a secret key for Django"""
    os.chdir(get_root_path())
    generate_secret_key_command = [
        "docker", "run", "--rm",
        PROJECT_NAME,
        "python generate_secret_key.py"
    ]
    run_command(" ".join(generate_secret_key_command))


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
    docker_run_command = [
        "docker run --rm",
        f"-e DJANGO_SETTINGS_MODULE={DEV_SETTINGS}",
        f"-e DJANGO_SECRET_KEY='{os.environ['DJANGO_SECRET_KEY']}'",
        "-p 8000:8000",
        PROJECT_NAME,
        f"python manage.py runserver 0.0.0.0:8000",
    ]
    run_command(" ".join(docker_run_command))


@task()
def run_prod():
    """Run production server"""
    # TODO: will require setting up a production server
    pass


@task()
def unit_test():
    docker_test = [
        "docker run --rm -it",
        PROJECT_NAME,
        "pytest",
    ]
    run_command(" ".join(docker_test))


def run_command(command):
    exit_code = os.system(command)
    if exit_code != 0:
        raise Exception(f"Command {command} failed with exit code {exit_code}")


def get_root_path():
    # TODO: maybe can be fancier?
    return pathlib.Path(__file__).resolve().parent.parent
