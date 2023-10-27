from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.helper.bcrypt as bcrypt
from src.helper.s3 import upload_photo as s3_upload_photo

import src.repository.usuario.select as usuario_select_repository
import src.repository.usuario.update as usuario_update_repository

def put(correo):
    try:
        new_correo = request.form.get('newCorreo')
        if not new_correo:
            return http_error_400('El campo `newCorreo` es obligatorio.')

        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        apellido = request.form.get('apellido')
        if not apellido:
            return http_error_400('El campo `apellido` es obligatorio.')

        contrasena = request.form.get('contrasena')
        if not contrasena:
            return http_error_400('El campo `contrasena` es obligatorio.')

        updated_picture = request.form.get('updatedPicture')
        if updated_picture:
            buffer = request.files.get('buffer')
            if not buffer or not buffer.filename:
                return http_error_400('El campo de imagen `buffer` es necesario si se va a editar la imagen.')

        user_dictionary = usuario_select_repository.login_user(correo)
        if not user_dictionary:
            return http_error_400('Este usuario no está registrado.')

        if correo != new_correo:
            user_exists = usuario_select_repository.get_usuario(new_correo)
            if user_exists:
                return http_error_400('Este correo ya está registrado, no se puede cambiar.')

        if not bcrypt.is_the_same(contrasena, user_dictionary.get('contrasena')):
            return http_error_400('Las credenciales son incorrectas.')

        if updated_picture:
            buffer = request.files.get('buffer')
            s3_upload_photo(buffer, user_dictionary.get('url_s3_foto'), True)

        usuario_update_repository.update_user(
            nombre,
            apellido,
            correo,
            new_correo
        )

        return http_ok_message_200('Usuario actualizado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar actualizar un usuario.')
