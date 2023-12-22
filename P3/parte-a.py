## PARTE A ##

'''
IMPORTANTE!
Para la pregunta 3 se modifico un poco la consulta de la pregunta 1 (tienen la misma esencia):
PARTE MODIFICADA:
    JOIN (
        SELECT
            product_id,
            MIN(normal_price) AS min_price,
            MAX(normal_price) AS max_price
        FROM
            Price
        WHERE
            active = 1
        GROUP BY
            product_id
    ) AS min_max_prices ON p.id = min_max_prices.product_id
    JOIN Price pr ON min_max_prices.product_id = pr.product_id AND (min_max_prices.min_price = pr.normal_price OR min_max_prices.max_price = pr.normal_price)

esta modificación permite obtener tanto el precio mínimo como el precio máximo activo para 
cada producto, la cual es necesaria para el 'rango de precios'.
'''
import sqlite3

def SQL_Consulta():
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
                MIN(normal_price) AS min_price,
                MAX(normal_price) AS max_price
            FROM
                Price
            WHERE
                active = 1
            GROUP BY
                product_id
        ) AS min_max_prices ON p.id = min_max_prices.product_id
        JOIN Price pr ON min_max_prices.product_id = pr.product_id AND (min_max_prices.min_price = pr.normal_price OR min_max_prices.max_price = pr.normal_price)
        JOIN Market m ON p.Market_id = m.id;
        """

        cursor.execute(sql_query)
        results = cursor.fetchall()

        return results

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

    finally:
        connection.close()

def agrupar_productos(datos_query):
    productos_agrupados = {}

    for producto in datos_query:
        ean = producto[1]  
        nombre = producto[0] 
        valores = producto[4]  
        markets_diferentes = producto[3] 

        if ean not in productos_agrupados:
            productos_agrupados[ean] = []

        rango_precios = producto[4]

        if len(producto) > 5 and producto[4] != producto[5]:  # Más de un precio
            rango_precios = f"{producto[5]} - {producto[4]}"  # Rango de precios

        productos_agrupados[ean].append({
            "nombre_producto": nombre,
            "valores": valores,
            "cantidad_markets_diferentes": markets_diferentes,
            "rango_precios": rango_precios
        })

    return productos_agrupados

datos_query = SQL_Consulta()

if datos_query:
    productos_agrupados = agrupar_productos(datos_query)
    print(productos_agrupados)
else:
    print("No se pudieron obtener los datos de la consulta.")
