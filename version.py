import subprocess

version = subprocess.check_output(["git", "describe", "--abbrev=0", "--tags"]).decode('ascii').strip()