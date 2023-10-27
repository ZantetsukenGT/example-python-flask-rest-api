from src.helper.db import get_db_conn

query_get_url_album = '''SELECT url_s3_foto FROM album WHERE id_album = %s'''

def get_url_album(id_album):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_album,)
        cursor.execute(query_get_url_album, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()
