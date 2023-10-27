from src.helper.db import get_db_conn

query_update_artista = '''UPDATE artista SET nombre = %s where id_artista = %s'''

def update_artista(nombre, id_artista):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (nombre, id_artista)
        cursor.execute(query_update_artista, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
