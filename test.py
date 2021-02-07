import subprocess

# subprocess.call('ls', shell=True)

name_dir = input("Ingresa el nombre del directorio ")

subprocess.call(f"mkdir {name_dir}", shell=True)
