import sqlite3

# Conectarse a la base de datos
connection = sqlite3.connect('CoolebraSPA.db')
cursor = connection.cursor()

try:
    sql_query = """
        SELECT
            p.Name AS Product_Name,
            p.EAN,
            p.SKU,
            m.Name AS Market_Name,
            pr.normal_price AS Last_Active_Min_Price
        FROM
            Product p
        JOIN (
            SELECT
                product_id,
                MIN(normal_price) AS min_price
            FROM
                Price
            WHERE
                active = 1
            GROUP BY
                product_id
        ) AS min_prices ON p.id = min_prices.product_id
        JOIN Price pr ON min_prices.product_id = pr.product_id AND min_prices.min_price = pr.normal_price
        JOIN Market m ON p.Market_id = m.id;
    """

    cursor.execute(sql_query)

    results = cursor.fetchall()

    for row in results:
        print(row)

except Exception as e:
    print(f"Error al ejecutar la consulta: {e}")

finally:
    connection.close()
