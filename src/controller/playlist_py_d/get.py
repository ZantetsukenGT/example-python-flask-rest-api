from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

import src.repository.playlist.select as playlist_select_repository
import src.repository.detalle_playlist.select as detalle_playlist_select_repository

def get_playlists(correo):
    try:
        playlists_list = playlist_select_repository.get_playlists(correo)

        return http_ok_json_200( { 'data': playlists_list } )
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar obtener las playlists de un usuario.')


def get_canciones_playlist(playlist):
    try:
        detalles_playlist_list = detalle_playlist_select_repository.get_detalles_playlist(playlist)

        return http_ok_json_200( { 'data': detalles_playlist_list } )
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar obtener el contenido de una playlist.')
