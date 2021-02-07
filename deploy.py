import subprocess

print("Descargando proyecto...")
subprocess.call("git clone https://github.com/johancastillo/ct-frontend.git", shell=True)

print("¿Cómo deseas instalar las dependencias del proyecto?")
print("a) Con NPM")
print("b) Con YARN")

# Options
a_one = "npm"
b_one = "yarn"

option_selected = input("Selecione una opción: ")

subprocess.call("cd ct-frontend", shell=True)

# Install dependencies
if option_selected == "a":
    subprocess.call(f"{a_one} i")
elif option_selected == "b":
    subprocess.call(f"{b_one}")
else:
    print("La opción no es válida")

# Run server development
print("¿Quieres ejecutar el servidor de desarrollo?")
print("a) ")



