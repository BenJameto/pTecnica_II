#!/bin/bash

# Crear el directorio si no existe
DIR="/home/jameto/Documentos/pTecnica_II/script"
if [ ! -d "$DIR" ]; then
    mkdir -p "$DIR"
fi

while true; do
    # Obtener la hora actual
    CURRENT_TIME=$(date +"%H:%M:%S")
    # Crear el mensaje
    MESSAGE="hola mundo, son las $CURRENT_TIME"
    # Guardar el mensaje en un archivo de texto
    echo "$MESSAGE" > "$DIR/mensaje_$(date +"%Y%m%d_%H%M%S").txt"
    # Esperar 1 minuto
    sleep 60
done
