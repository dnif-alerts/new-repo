import subprocess
import os


subprocess.call(f'rm -r {os.environ["DIR"]}')
