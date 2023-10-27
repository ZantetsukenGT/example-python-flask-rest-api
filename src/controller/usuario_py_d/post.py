from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.helper.bcrypt as bcrypt
from src.helper.s3 import upload_photo as s3_upload_photo
from uuid import uuid4

import src.repository.usuario.select as usuario_select_repository
import src.repository.usuario.insert as usuario_insert_repository

def login():
    try:
        correo = request.form.get('correo')
        if not correo:
            return http_error_400('El campo `correo` es obligatorio.')

        contrasena = request.form.get('contrasena')
        if not contrasena:
            return http_error_400('El campo `contrasena` es obligatorio.')

        user_dictionary = usuario_select_repository.login_user(correo)
        if not user_dictionary:
            return http_error_400('Las credenciales son incorrectas.')

        if not bcrypt.is_the_same(contrasena, user_dictionary.get('contrasena')):
            return http_error_400('Las credenciales son incorrectas.')
        print(user_dictionary)
        return http_ok_json_200({ 'message': 'Inicio de sesión exitoso.', 'id_rol': user_dictionary.get('id_rol') })
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar iniciar sesión.')


def register():
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        apellido = request.form.get('apellido')
        if not apellido:
            return http_error_400('El campo `apellido` es obligatorio.')

        correo = request.form.get('correo')
        if not correo:
            return http_error_400('El campo `correo` es obligatorio.')

        contrasena = request.form.get('contrasena')
        if not contrasena:
            return http_error_400('El campo `contrasena` es obligatorio.')

        fecha = request.form.get('fecha')
        if not fecha:
            return http_error_400('El campo `fecha` es obligatorio.')

        buffer = request.files.get('buffer')
        if not buffer or not buffer.filename:
            return http_error_400('El campo de imagen `buffer` es obligatorio.')

        user_dictionary = usuario_select_repository.login_user(correo)
        if user_dictionary:
            return http_error_400('Este correo ya está registrado.')

        hashed_password = bcrypt.hash(contrasena)

        file_extension = buffer.filename.split('.')[-1]
        filename = f'{str(uuid4())}.{file_extension}'
        url_s3_foto = s3_upload_photo(buffer, filename, False)

        usuario_insert_repository.register_user(
            nombre,
            apellido,
            url_s3_foto,
            correo,
            hashed_password,
            fecha
        )

        return http_ok_message_200('Usuario registrado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar un usuario.')
