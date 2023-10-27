from src.helper.db import get_db_conn
from uuid import uuid4

query_register_user = '''INSERT INTO usuario (id_usuario, nombre, apellido, url_s3_foto, correo, contrasena, fechanac)
VALUES (%s,%s,%s,%s,%s,%s,%s)'''

def register_user(nombre, apellido, url_s3_foto, correo, hashed_password, fecha_nacimiento):
    db_conn = get_db_conn()
    try:
        cursor = db_conn.cursor(prepared = True, dictionary = True)

        values = ([str(uuid4()), nombre, apellido, url_s3_foto, correo, hashed_password, fecha_nacimiento])
        cursor.execute(query_register_user, values)

        db_conn.commit()
    except:
        db_conn.rollback()
        raise
    finally:
        cursor.close()
        db_conn.close()
