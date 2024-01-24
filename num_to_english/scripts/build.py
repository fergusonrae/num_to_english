
import os
from scripts.config import PROJECT_NAME
from scripts.utils import run_command, get_root_path


os.chdir(get_root_path())
docker_build_command = [
    "docker", "build",
    "-t", PROJECT_NAME,
    "."
]
run_command(" ".join(docker_build_command))
