from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.favorito.select as favorito_select_repository

def get(correo):
    try:
        favoritos_list = favorito_select_repository.get_favoritos(correo)

        return http_ok_json_200( { 'data': favoritos_list } )
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar obtener los favoritos de un usuario.')
