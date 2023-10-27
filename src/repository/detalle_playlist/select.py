from src.helper.db import get_db_conn

query_get_detalles_playlist = '''SELECT c.* FROM cancion c
INNER JOIN detalle_playlist dp ON c.id_cancion = dp.id_cancion
WHERE dp.id_playlist = %s'''

def get_detalles_playlist(id_playlist):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_playlist,)
        cursor.execute(query_get_detalles_playlist, values)

        return cursor.fetchall()
    finally:
        cursor.close()
        db_conn.close()
