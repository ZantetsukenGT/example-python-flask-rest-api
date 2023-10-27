from src.helper.db import get_db_conn

query_update_album = '''UPDATE album SET nombre = %s, descripcion = %s where id_album = %s'''

def update_album(nombre, descripcion, id_album):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (nombre, descripcion, id_album)
        cursor.execute(query_update_album, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
