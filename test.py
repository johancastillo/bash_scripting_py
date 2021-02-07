import subprocess

# subprocess.call('ls', shell=True)

name_dir = input("Ingresa el nombre del directorio ")

subprocess.call(f"mkdir {name_dir} {name_dir}/build {name_dir}/src {name_dir}/src/pug {name_dir}/src/scss {name_dir}/src/ts", shell=True)

subprocess.call(f"ls {name_dir}", shell=True)
