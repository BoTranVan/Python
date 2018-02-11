import subprocess

for i in range(10):
    subprocess.Popen(["python", "threads.py", "100"])
