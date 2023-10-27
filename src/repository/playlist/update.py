from src.helper.db import get_db_conn

query_update_playlist = '''UPDATE playlist SET nombre = %s, descripcion = %s, url_s3_foto = %s where id_playlist = %s'''

def update_playlist(nombre, descripcion, url_s3_foto, id_playlist):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (nombre, descripcion, url_s3_foto, id_playlist)
        cursor.execute(query_update_playlist, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
