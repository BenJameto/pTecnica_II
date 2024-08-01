#!/bin/bash

# Directorio a respaldar
DIR="/home/jameto/Documentos/pTecnica_II/script"

# Bucket de S3
BUCKET_NAME="jameto"

# Archivo de log
LOG_FILE="/home/jameto/Documentos/pTecnica_II/script/backup_log.txt"

while true; do
    # Fecha y hora actual
    TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

    # Archivo de respaldo
    BACKUP_FILE="/tmp/backup_$TIMESTAMP.tar.gz"

    # Crear un archivo tar.gz del directorio
    tar -czf "$BACKUP_FILE" -C "$DIR" .

    # Subir el archivo a S3 y capturar errores
    if aws s3 cp "$BACKUP_FILE" "s3://$BUCKET_NAME/" 2>> "$LOG_FILE"; then
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Backup successfully uploaded: $BACKUP_FILE" >> "$LOG_FILE"
    else
        echo "[$(date +"%Y-%m-%d %H:%M:%S")] Failed to upload backup: $BACKUP_FILE" >> "$LOG_FILE"
    fi

    # Eliminar el archivo temporal
    rm "$BACKUP_FILE"

    # Esperar 10 minutos
    sleep 600
done
