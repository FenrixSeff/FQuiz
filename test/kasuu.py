import subprocess

up = subprocess.run(
    ["git", "log", "--oneline", "--graph"],
    capture_output=True, text=True
)
dft = up.stdout.splitlines()

for n, d in enumerate(dft):
    if n == 10:
        break
    print(d)
