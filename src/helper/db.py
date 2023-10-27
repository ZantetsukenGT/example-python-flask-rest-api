from mysql.connector.pooling import MySQLConnectionPool
from src.config.db_config import db_config

cnxpool = MySQLConnectionPool(pool_name = "mydatabase", pool_size = 10, **db_config)

def get_db_conn():
    return cnxpool.get_connection()
