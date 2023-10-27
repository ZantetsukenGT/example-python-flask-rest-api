from src.helper.db import get_db_conn

query_delete_playlist1 = '''DELETE FROM detalle_playlist WHERE id_playlist = %s'''
query_delete_playlist2 = '''DELETE FROM playlist WHERE id_playlist = %s'''

def delete_playlist(id_playlist):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_playlist,)
        cursor.execute(query_delete_playlist1, values)
        cursor.execute(query_delete_playlist2, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
