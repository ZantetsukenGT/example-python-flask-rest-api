from src.helper.db import get_db_conn

query_get_historial = '''SELECT h.* FROM historial h
INNER JOIN cancion c ON h.id_cancion = c.id_cancion
WHERE h.id_usuario = (SELECT id_usuario FROM usuario WHERE correo = %s)'''

def get_historial(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_get_historial, values)

        return cursor.fetchall()
    finally:
        cursor.close()
        db_conn.close()
