from src.helper.db import get_db_conn
from uuid import uuid4

query_register_favorito = '''INSERT INTO favorito (id_usuario, id_cancion)
VALUES (%s,%s)'''

def register_favorito(id_usuario, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_usuario, id_cancion)
        cursor.execute(query_register_favorito, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
