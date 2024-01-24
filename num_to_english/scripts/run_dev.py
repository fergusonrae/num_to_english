import os
from config import DEV_SETTINGS, PROJECT_NAME
from utils import run_command

docker_run_command = [
    "docker run --rm -it",
    f"-e DJANGO_SETTINGS_MODULE={DEV_SETTINGS}",
    f"-e DJANGO_SECRET_KEY='{os.environ['DJANGO_SECRET_KEY']}'",
    "-p 8000:8000",
    PROJECT_NAME,
    f"python manage.py runserver 0.0.0.0:8000",
]
run_command(" ".join(docker_run_command))
