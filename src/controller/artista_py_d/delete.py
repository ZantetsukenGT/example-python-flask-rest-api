from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.artista.delete as artista_delete_repository

def delete(artista):
    try:
        artista_delete_repository.delete_artista(
            artista
        )

        return http_ok_message_200('Artista eliminado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar eliminar un artista.')
