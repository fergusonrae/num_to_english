import os
from config import PROJECT_NAME
from utils import run_command, get_root_path


os.chdir(get_root_path())
generate_secret_key_command = [
    "docker", "run", "--rm", '-it',
    PROJECT_NAME,
    "python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'"
]
run_command(" ".join(generate_secret_key_command))
