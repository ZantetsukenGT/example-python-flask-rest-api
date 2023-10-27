from src.helper.db import get_db_conn

query_get_urls_cancion = '''SELECT url_s3_foto, url_s3_mp3 FROM cancion WHERE id_cancion = %s'''

def get_urls_cancion(id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_cancion,)
        cursor.execute(query_get_urls_cancion, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()
