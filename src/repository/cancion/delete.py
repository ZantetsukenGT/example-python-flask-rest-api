from src.helper.db import get_db_conn

query_delete_cancion1 = '''DELETE FROM favorito WHERE id_cancion = %s'''
query_delete_cancion2 = '''DELETE FROM detalle_playlist WHERE id_cancion = %s'''
query_delete_cancion3 = '''DELETE FROM cancion WHERE id_cancion = %s'''

def delete_cancion(id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_cancion,)
        cursor.execute(query_delete_cancion1, values)
        cursor.execute(query_delete_cancion2, values)
        cursor.execute(query_delete_cancion3, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
