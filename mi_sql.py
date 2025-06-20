import mysql.connector

def conectar(consulta_sql, parametros=None):
    # Credenciales para la conexión
    config = {
        'user': 'umusy3785azp07ek',
        'password': '8c3YxusE4cEI4a8Pcb31',
        'host': 'bxhsiwlhpucuefabwea0-mysql.services.clever-cloud.com',
        'database': 'bxhsiwlhpucuefabwea0',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**config)
        print("Conexión exitosa a la base de datos.")

        # Crear cursor
        consulta = conexion.cursor()
        
        # Ejecutar consulta con parámetros si existen
        if parametros:
            consulta.execute(consulta_sql, parametros)
        else:
            consulta.execute(consulta_sql)
        
        # Determinar si es una consulta de selección
        if consulta_sql.strip().lower().startswith("select"):
            resultado = consulta.fetchall()
            consulta.close()
            conexion.close()
            return resultado
        else:
            # Para INSERT, UPDATE, DELETE, hacer commit
            conexion.commit()
            filas_afectadas = consulta.rowcount
            consulta.close()
            conexion.close()
            return filas_afectadas

    except mysql.connector.Error as err:
        error_msg = f"Error MySQL ({err.errno}): {err.msg}"
        print(error_msg)
        raise Exception(error_msg) from err