from src.helper.db import get_db_conn
from uuid import uuid4

query_register_historial = '''INSERT INTO historial (id_historial, id_usuario, id_cancion)
VALUES (%s,%s,%s)'''

def register_historial(id_usuario, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (str(uuid4()), id_usuario, id_cancion)
        cursor.execute(query_register_historial, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
