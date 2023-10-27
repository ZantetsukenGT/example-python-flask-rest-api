from src.helper.db import get_db_conn

query_update_user = '''UPDATE usuario SET nombre = %s, apellido = %s, correo = %s WHERE correo = %s'''

def update_user(nombre, apellido, correo, new_correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (nombre, apellido, new_correo, correo)
        cursor.execute(query_update_user, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
