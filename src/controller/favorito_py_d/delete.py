from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.usuario.select as usuario_select_repository
import src.repository.favorito.delete as favorito_delete_repository

def delete(correo, cancion):
    try:
        user_dictionary = usuario_select_repository.login_user(correo)
        if not user_dictionary:
            return http_error_400('Este usuario no está registrado.')

        favorito_delete_repository.delete_favorito(
            user_dictionary.get('id_usuario'),
            cancion
        )

        return http_ok_message_200('Canción eliminada de los favoritos correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar eliminar una canción de los favoritos.')
