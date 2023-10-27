from src.helper.db import get_db_conn
from uuid import uuid4

query_register_playlist = '''INSERT INTO playlist (id_playlist, nombre, descripcion, url_s3_foto, id_usuario)
VALUES (%s,%s,%s,%s,%s)'''

def register_playlist(nombre, descripcion, url_s3_foto, id_usuario):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (str(uuid4()), nombre, descripcion, url_s3_foto, id_usuario)
        cursor.execute(query_register_playlist, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
