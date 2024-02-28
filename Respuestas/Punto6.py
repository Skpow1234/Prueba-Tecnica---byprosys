import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('pruebaByprosys.db')
cursor = conn.cursor()

# Consulta SQL para obtener el total de transacciones conciliables de BANSUR que no cruzaron contra CLAP
query_no_cruzadas = """
    SELECT COUNT(*)
    FROM BANSUR
    WHERE SUBSTR(TARJETA, 1, 6) || SUBSTR(TARJETA, -4) NOT IN (
        SELECT INICIO6_TARJETA || FINAL4_TARJETA
        FROM CLAP
    )
    AND FECHA_TRANSACCION IN (
        SELECT FECHA_TRANSACCION
        FROM CLAP
    )
"""

# Ejecutar la consulta para obtener el total de transacciones conciliables de BANSUR que no cruzaron contra CLAP
cursor.execute(query_no_cruzadas)
total_no_cruzadas = cursor.fetchone()[0]

# Consulta SQL para obtener el total de transacciones conciliables de BANSUR
query_total = "SELECT COUNT(*) FROM BANSUR"

# Ejecutar la consulta para obtener el total de transacciones conciliables de BANSUR
cursor.execute(query_total)
total_bansur = cursor.fetchone()[0]

# Calcular el porcentaje de transacciones no cruzadas
porcentaje_no_cruzadas = (total_no_cruzadas / total_bansur) * 100

print(f"El porcentaje de transacciones de BANSUR que no cruzaron contra CLAP es: {porcentaje_no_cruzadas:.2f}%")

# Cerrar la conexión a la base de datos
conn.close()
