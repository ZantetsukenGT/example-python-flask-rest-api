from src.helper.db import get_db_conn
from uuid import uuid4

query_register_detalle_playlist = '''INSERT INTO detalle_playlist (id_playlist, id_cancion)
VALUES (%s,%s)'''

def register_detalle_playlist(id_playlist, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_playlist, id_cancion)
        cursor.execute(query_register_detalle_playlist, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
