import shlex
import subprocess


def get_disk_usage(parameters: str):
    command = ["df", "-h"] + shlex.split(parameters)

    try:
        result = subprocess.run(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False
        )
        usage = result.stdout.strip().decode()
    except:
        raise Exception("An unexpected error was observed")

    return usage
