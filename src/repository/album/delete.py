from src.helper.db import get_db_conn

query_delete_album1 = '''UPDATE cancion SET id_album = NULL where id_album = %s'''
query_delete_album2 = '''DELETE FROM album WHERE id_album = %s'''

def delete_album(id_album):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_album,)
        cursor.execute(query_delete_album1, values)
        cursor.execute(query_delete_album2, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
