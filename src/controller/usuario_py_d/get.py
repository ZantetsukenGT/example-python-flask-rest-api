from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.usuario.select as usuario_select_repository

def get(correo):
    try:
        user_dictionary = usuario_select_repository.get_usuario(correo)
        if not user_dictionary:
            return http_error_400('Este usuario no está registrado.')

        return http_ok_json_200( { 'data': [user_dictionary] } )
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar obtener la info. de un usuario.')
