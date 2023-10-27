from src.helper.db import get_db_conn

query_get_playlists = '''SELECT * FROM playlist
WHERE id_usuario = (SELECT id_usuario FROM usuario WHERE correo = %s)'''

def get_playlists(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_get_playlists, values)

        return cursor.fetchall()
    finally:
        cursor.close()
        db_conn.close()
