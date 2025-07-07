import os
from psycopg2 import pool
from dotenv import load_dotenv

#Cargamos el archivo .env
load_dotenv()

#Obtenemos el string de conexion del .env
connection_string=os.getenv('DATA_BASE_URL')
#Creamos un pool de conexiones
connection_pool=pool.SimpleConnectionPool(
    1,
    5,
    connection_string
)

if connection_pool:
    print("Pool creado exitosamente")

#Obtenemos una conexion del pool
conn=connection_pool.getconn()

#Creamos un cursor
cursor=conn.cursor()
cursor.execute("SELECT NOW()")
time=cursor.fetchone()[0]
cursor.close()
connection_pool.putconn(conn)
connection_pool.closeall()
print("Current Time: ",time)
