import os
from config import PROJECT_NAME
from utils import run_command

# TODO: create separate test settings
docker_test = [
    "docker run --rm -it",
    "-e DJANGO_SETTINGS_MODULE=num_to_english.settings.development",
    f"-e DJANGO_SECRET_KEY='{os.environ['DJANGO_SECRET_KEY']}'",
    PROJECT_NAME,
    "python manage.py test",
]
run_command(" ".join(docker_test))
