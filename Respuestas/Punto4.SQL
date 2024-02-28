WITH conciliables AS (
    SELECT 
        clap.*,
        bansur.*,
        CASE
            WHEN clap.INICIO6_TARJETA || clap.FINAL4_TARJETA = SUBSTR(bansur.TARJETA, 1, 6) || SUBSTR(bansur.TARJETA, -4)
                AND clap.FECHA_TRANSACCION = bansur.FECHA_TRANSACCION
                AND ABS(clap.MONTO - bansur.MONTO) <= 0.99 THEN 'Sí'
            ELSE 'No'
        END AS cruzo_contrapartida,
        ROW_NUMBER() OVER (ORDER BY clap.FECHA_TRANSACCION, clap.ID_BANCO) AS conciliacion_id
    FROM CLAP clap
    INNER JOIN BANSUR bansur ON clap.FECHA_TRANSACCION = bansur.FECHA_TRANSACCION
)
SELECT * FROM conciliables;
