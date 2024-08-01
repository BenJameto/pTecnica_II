import subprocess

def run_command(command):
    """Ejecuta un comando en la terminal con sudo y muestra su salida."""
    process = subprocess.Popen(f"sudo {command}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error al ejecutar el comando '{command}': {stderr.decode()}")
    else:
        print(stdout.decode())

def deploy_docker_container(image_name, container_name, port_mapping):
    """Despliega un contenedor Docker con la imagen y configuración especificadas."""
    # Detener y eliminar contenedor si existe
    run_command(f"docker stop {container_name} || true")
    run_command(f"docker rm {container_name} || true")
    
    # Ejecutar el contenedor
    run_command(f"docker run -d --name {container_name} -p {port_mapping} {image_name}")

# Configuración para Nginx
image_name = "nginx"  # Nombre de la imagen Docker para Nginx
container_name = "my-nginx-container"  # Nombre del contenedor
port_mapping = "8080:80"  # Mapeo de puertos (puerto local:puerto del contenedor)

# Desplegar el contenedor
deploy_docker_container(image_name, container_name, port_mapping)
