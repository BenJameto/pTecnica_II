import psycopg2
import os
import logging
from dotenv import load_dotenv

# Configuración de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Cargar variables de entorno
load_dotenv()


def lee_query(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def lee_datos(filepath):
    with open(filepath, 'r') as file:
        return [line.strip().split(',') for line in file]
    
def ejecutar_query(query, params=None, buscar_resultados=False):
    try:
        conexion = psycopg2.connect(
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        cursor = conexion.cursor()
        cursor.execute(query, params)
        if buscar_resultados:
            resultados = cursor.fetchall()
            cursor.close()
            conexion.close()
            return resultados
        conexion.commit()
        cursor.close()
        conexion.close()
    except Exception as error:
        logger.error(f"Error al ejecutar la consulta: {error}")

def main():
    try:
        eliminar_tabla_query = "DROP TABLE IF EXISTS motos;"
        ejecutar_query(eliminar_tabla_query)
        logger.info("se borro la tabla anterior exitosamente")
    except Exception as error:
        logger.error(f"error al intntar borrar la tabla: {error}")
        
    
    # Se lee el archivo SQL
    crear_tabla = lee_query('query.sql')
    ejecutar_query(crear_tabla)
    
    # Lee el archivo de motos
    try:
        datos_motos = lee_datos('data/motos.txt')
        logger.info("se ingresaron todos los datos de manera correcta")
    except Exception as error:
        logger.error(f"Error al cargar los datos: {error}")
    
    # Insertar datos de motos si no existen
    insertar_query = """
    INSERT INTO motos (marca, nombre, cilindrada) 
    VALUES (%s, %s, %s) 
    ON CONFLICT (marca, nombre, cilindrada) DO NOTHING;
    """
    for moto in datos_motos:
        ejecutar_query(insertar_query, moto)
    
    # Seleccionar motos de la marca kawasaki
    seleccionar_query = "SELECT * FROM motos WHERE marca = 'kawasaki';"
    resultados = ejecutar_query(seleccionar_query, buscar_resultados=True)
    if resultados:
        logger.info("Motos de la marca Kawasaki:")
        for resultado in resultados:
            logger.info(resultado)
    else:
        logger.info("No se encontraron motos de la marca Kawasaki")
            
if __name__ == "__main__":
    main()
