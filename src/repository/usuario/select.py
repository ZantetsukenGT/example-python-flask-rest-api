from src.helper.db import get_db_conn

query_login_user = '''SELECT id_usuario, contrasena, url_s3_foto, id_rol FROM usuario WHERE correo = %s'''

def login_user(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_login_user, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()


query_get_usuario = '''SELECT nombre, apellido, id_rol FROM usuario WHERE correo = %s'''

def get_usuario(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_get_usuario, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()


query_url_usuario = '''SELECT url_s3_foto FROM usuario WHERE correo = %s'''

def get_url_s3_foto_usuario(correo):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = (correo,)
        cursor.execute(query_url_usuario, values)

        return cursor.fetchone()
    finally:
        cursor.close()
        db_conn.close()
