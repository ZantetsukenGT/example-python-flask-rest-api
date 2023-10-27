from src.helper.db import get_db_conn

query_delete_favorito = '''DELETE FROM favorito WHERE id_usuario = %s AND id_cancion = %s'''

def delete_favorito(id_usuario, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_usuario, id_cancion)
        cursor.execute(query_delete_favorito, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
