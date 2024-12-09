import os
import subprocess

# Define el nombre de tu proyecto
project_name = "mi_app"

# 1. Crear el directorio del proyecto
os.makedirs(project_name, exist_ok=True)
os.chdir(project_name)

# 2. Configurar entorno virtual
print("Creando el entorno virtual...")
subprocess.run(["python3", "-m", "venv", ".venv"])
print("Activando el entorno virtual...")
subprocess.run(["source", ".venv/bin/activate"], shell=True, executable="/bin/bash")

# 3. Instalar Reflex
print("Instalando Reflex...")
subprocess.run(["pip", "install", "reflex"])

# 4. Inicializar el proyecto
print("Inicializando el proyecto...")
subprocess.run(["reflex", "init"])

# 5. Ejecutar la aplicación en modo desarrollo
print("Ejecutando la aplicación en modo desarrollo...")
subprocess.run(["reflex", "run"])
