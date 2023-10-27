from src.helper.db import get_db_conn

query_delete_artista1 = '''DELETE FROM favorito WHERE id_cancion IN 
(SELECT id_cancion FROM cancion WHERE id_artista = %s)'''
query_delete_artista2 = '''DELETE FROM detalle_playlist WHERE id_cancion IN 
(SELECT id_cancion FROM cancion WHERE id_artista = %s)'''
query_delete_artista3 = '''DELETE FROM cancion WHERE id_artista = %s'''
query_delete_artista4 = '''DELETE FROM album WHERE id_artista = %s'''
query_delete_artista5 = '''DELETE FROM artista WHERE id_artista = %s'''

def delete_artista(id_artista):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (id_artista,)
        cursor.execute(query_delete_artista1, values)
        cursor.execute(query_delete_artista2, values)
        cursor.execute(query_delete_artista3, values)
        cursor.execute(query_delete_artista4, values)
        cursor.execute(query_delete_artista5, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
