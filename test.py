import subprocess
import os


subprocess.call(f'rm -r {os.environ["DIR"]}', shell=True)
subprocess.call(f'rm -rf {os.environ["DIR"]}', shell=True)
