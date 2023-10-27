from src.helper.db import get_db_conn
from uuid import uuid4

query_register_album = '''INSERT INTO album (id_album, nombre, descripcion, url_s3_foto, id_artista)
VALUES (%s,%s,%s,%s,%s)'''

def register_album(nombre, descripcion, url_s3_foto, id_artista):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (str(uuid4()), nombre, descripcion, url_s3_foto, id_artista)
        cursor.execute(query_register_album, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
