from src.helper.db import get_db_conn

query_get_url_artista = '''SELECT url_s3_foto FROM artista WHERE id_artista = %s'''

def get_url_artista(id_artista):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_artista,)
        cursor.execute(query_get_url_artista, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()
