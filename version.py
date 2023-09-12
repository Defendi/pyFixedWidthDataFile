import subprocess

version = subprocess.check_output(["git", "describe", "--tags"]).decode('ascii').strip()