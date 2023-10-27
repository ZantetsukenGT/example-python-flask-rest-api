from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.playlist.delete as playlist_delete_repository
import src.repository.detalle_playlist.delete as detalle_playlist_delete_repository

def delete_playlist(playlist):
    try:
        playlist_delete_repository.delete_playlist(
            playlist
        )

        return http_ok_message_200('Playlist eliminada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar eliminar una playlist.')


def delete_cancion_playlist(playlist, cancion):
    try:
        detalle_playlist_delete_repository.delete_detalle_playlist(
            playlist,
            cancion
        )

        return http_ok_message_200('Canción eliminada de la playlist correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar eliminar una canción de una playlist.')
