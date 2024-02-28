import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('pruebaByprosys.db')
cursor = conn.cursor()

# Consulta SQL para obtener el total de transacciones conciliables de CLAP que cruzaron contra BANSUR
query_cruzadas = """
    SELECT COUNT(*)
    FROM CLAP
    WHERE INICIO6_TARJETA || FINAL4_TARJETA IN (
        SELECT SUBSTR(TARJETA, 1, 6) || SUBSTR(TARJETA, -4)
        FROM BANSUR
    )
    AND FECHA_TRANSACCION IN (
        SELECT FECHA_TRANSACCION
        FROM BANSUR
    )
"""

# Ejecutar la consulta para obtener el total de transacciones conciliables de CLAP que cruzaron contra BANSUR
cursor.execute(query_cruzadas)
total_cruzadas = cursor.fetchone()[0]

# Consulta SQL para obtener el total de transacciones conciliables de CLAP
query_total = "SELECT COUNT(*) FROM CLAP"

# Ejecutar la consulta para obtener el total de transacciones conciliables de CLAP
cursor.execute(query_total)
total_clap = cursor.fetchone()[0]

# Calcular el porcentaje de transacciones cruzadas
porcentaje_cruzadas = (total_cruzadas / total_clap) * 100

print(f"El porcentaje de transacciones de CLAP que cruzaron contra BANSUR es: {porcentaje_cruzadas:.2f}%")

# Cerrar la conexión a la base de datos
conn.close()
