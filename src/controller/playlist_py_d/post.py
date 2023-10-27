from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo
from uuid import uuid4

import src.repository.playlist.insert as playlist_insert_repository
import src.repository.detalle_playlist.insert as detalle_playlist_insert_repository

def registrar_playlist():
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        id_usuario = request.form.get('id_usuario')
        if not id_usuario:
            return http_error_400('El campo `id_usuario` es obligatorio.')

        buffer = request.files.get('buffer')
        if not buffer or not buffer.filename:
            return http_error_400('El campo de imagen `buffer` es obligatorio.')

        descripcion = request.form.get('descripcion')
        if not descripcion:
            descripcion = None

        file_extension = buffer.filename.split('.')[-1]
        filename = f'{str(uuid4())}.{file_extension}'
        url_s3_foto = s3_upload_photo(buffer, filename, False)

        playlist_insert_repository.register_playlist(
            nombre,
            descripcion,
            url_s3_foto,
            id_usuario
        )

        return http_ok_message_200('Playlist registrada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar una playlist.')


def registrar_detalle_playlist():
    try:
        playlist = request.form.get('playlist')
        if not playlist:
            return http_error_400('El campo `playlist` es obligatorio.')

        cancion = request.form.get('cancion')
        if not cancion:
            return http_error_400('El campo `cancion` es obligatorio.')

        detalle_playlist_insert_repository.register_detalle_playlist(
            playlist,
            cancion
        )

        return http_ok_message_200('Ítem de playlist registrado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar un ítem de playlist.')
