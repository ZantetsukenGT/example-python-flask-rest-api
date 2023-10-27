from src.helper.db import get_db_conn
from uuid import uuid4

query_register_artista = '''INSERT INTO artista (id_artista, nombre, url_s3_foto, fechanac)
VALUES (%s,%s,%s,%s)'''

def register_artista(nombre, url_s3_foto, fecha_nacimiento):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (str(uuid4()), nombre, url_s3_foto, fecha_nacimiento)
        cursor.execute(query_register_artista, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
