import os
import pathlib


def run_command(command):
    exit_code = os.system(command)
    if exit_code != 0:
        raise Exception(f"Command {command} failed with exit code {exit_code}")


def get_root_path():
    # TODO: maybe can be fancier?
    return pathlib.Path(__file__).resolve().parent.parent.parent
