# Comparación de Tasas de Conciliación entre CLAP y BANSUR

Para comparar las cifras de las transacciones conciliables respecto a las cifras totales en las fuentes desde un punto de vista del negocio, podemos calcular la tasa de conciliación y analizar su impacto. La tasa de conciliación nos indicará qué porcentaje de las transacciones en una base de datos se consideran conciliables con respecto a la otra base de datos. Esto nos ayudará a entender la precisión y la integridad de los datos entre las dos fuentes.

La tasa de conciliación se puede calcular de la siguiente manera:

Tasa de Conciliación (%) = (Cantidad de Transacciones Conciliables / Cantidad Total de Transacciones) * 100

Entonces, podemos calcular la tasa de conciliación para ambas bases de datos y compararlas para evaluar la consistencia de los datos entre CLAP y BANSUR.

## Ejemplo de Cálculo de Tasa de Conciliación

Supongamos que tenemos los siguientes resultados de las consultas SQL:

**Para CLAP:**

- Cantidad de Transacciones Conciliables: 10,000
- Cantidad Total de Transacciones: 50,000

**Para BANSUR:**

- Cantidad de Transacciones Conciliables: 8,000
- Cantidad Total de Transacciones: 45,000

Podemos calcular la tasa de conciliación para cada base de datos:

**Para CLAP:**
Tasa de Conciliación CLAP = (10,000 / 50,000) * 100 = 20%

**Para BANSUR:**
Tasa de Conciliación BANSUR = (8,000 / 45,000) * 100 = 17.78%

Luego, podemos comparar estas tasas de conciliación para determinar qué base de datos tiene una mayor proporción de transacciones conciliables en relación con su cantidad total de transacciones. Una tasa de conciliación más alta indica una mayor integridad de los datos y una concordancia más precisa entre las dos fuentes. Si hay una discrepancia significativa entre las tasas de conciliación de ambas bases de datos, podría indicar problemas en la calidad de los datos o en los procesos de registro de transacciones.
