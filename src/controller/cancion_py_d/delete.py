from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.cancion.delete as cancion_delete_repository

def delete(cancion):
    try:
        cancion_delete_repository.delete_cancion(
            cancion
        )

        return http_ok_message_200('Canción eliminada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar eliminar una canción.')
