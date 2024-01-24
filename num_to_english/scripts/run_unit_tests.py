import os
from scripts.config import PROJECT_NAME
from scripts.utils import run_command

# TODO: create separate test settings
docker_test = [
    "docker run --rm -it",
    "-e DJANGO_SETTINGS_MODULE=num_to_english.settings.development",
    f"-e DJANGO_SECRET_KEY='{os.environ['DJANGO_SECRET_KEY']}'",
    PROJECT_NAME,
    "pytest",
]
run_command(" ".join(docker_test))
