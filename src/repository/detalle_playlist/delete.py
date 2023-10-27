from src.helper.db import get_db_conn

query_delete_detalle_playlist = '''DELETE FROM detalle_playlist WHERE id_playlist = %s AND id_cancion = %s'''

def delete_detalle_playlist(id_playlist, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_playlist, id_cancion)
        cursor.execute(query_delete_detalle_playlist, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
