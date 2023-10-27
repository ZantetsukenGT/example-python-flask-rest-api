from src.helper.db import get_db_conn

query_update_album_cancion = '''UPDATE cancion SET id_album = %s where id_cancion = %s'''

def update_album_cancion(id_album, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_album, id_cancion)
        cursor.execute(query_update_album_cancion, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()


query_update_cancion = '''UPDATE cancion SET nombre = %s, duracion = %s where id_cancion = %s'''

def update_cancion(nombre, duracion, id_cancion):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (nombre, duracion, id_cancion)
        cursor.execute(query_update_cancion, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
