from src.helper.db import get_db_conn

query_get_favoritos = '''SELECT c.* FROM cancion c
INNER JOIN favorito f ON c.id_cancion = f.id_cancion
WHERE f.id_usuario = (SELECT id_usuario FROM usuario WHERE correo = %s)'''

def get_favoritos(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_get_favoritos, values)

        return cursor.fetchall()
    finally:
        cursor.close()
        db_conn.close()
