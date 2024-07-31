import psycopg2

def lee_query(filepath):
    with open(filepath, 'r') as file:
        return file.read()
    
def lee_datos(filepath):
    with open(filepath, 'r') as file:
        return [line.strip().split(',') for line in file]
    
def ejecutar_query(query, params=None, buscar_resultados=False):
    try:
        conexion = psycopg2.connect(
            dbname="prueba",
            user="usuario",
            password="contrasegna",
            host="localhost",
            port="5432"
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
        print(f"Error al ejecutar la consulta: {error}")

def main():
    # Se lee el archivo SQL
    crear_tabla = lee_query('query.sql')
    ejecutar_query(crear_tabla)
    
    # Lee el archivo de motos
    datos_motos = lee_datos('data/motos.txt')
    
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
        for resultado in resultados:
            print(resultado)
            
if __name__ == "__main__":
    main()
