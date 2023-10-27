from src.helper.db import get_db_conn
from uuid import uuid4

query_register_cancion = '''INSERT INTO cancion (id_cancion, nombre, url_s3_foto, url_s3_mp3, id_artista, duracion, id_album)
VALUES (%s,%s,%s,%s,%s,%s,%s)'''

def register_cancion(nombre, url_s3_foto, url_s3_mp3, id_artista, duracion, id_album):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (str(uuid4()), nombre, url_s3_foto, url_s3_mp3, id_artista, duracion, id_album)
        cursor.execute(query_register_cancion, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
