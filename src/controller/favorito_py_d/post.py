from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.favorito.insert as favorito_insert_repository

def post():
    try:
        id_usuario = request.form.get('id_usuario')
        if not id_usuario:
            return http_error_400('El campo `id_usuario` es obligatorio.')

        cancion = request.form.get('cancion')
        if not cancion:
            return http_error_400('El campo `cancion` es obligatorio.')

        favorito_insert_repository.register_favorito(
            id_usuario,
            cancion
        )

        return http_ok_message_200('Canción favorita registrada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar una canción favorita.')
