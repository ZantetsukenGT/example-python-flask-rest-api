from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo
from src.helper.s3 import upload_audio as s3_upload_audio

import src.repository.cancion.select as cancion_select_repository
import src.repository.cancion.update as cancion_update_repository

def update_cancion(cancion):
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        duracion = request.form.get('duracion')
        if not duracion:
            return http_error_400('El campo `duracion` es obligatorio.')

        updated_picture = request.form.get('updatedPicture')
        if updated_picture:
            buffer = request.files.get('buffer')
            if not buffer or not buffer.filename:
                return http_error_400('El campo de imagen `buffer` es necesario si se va a editar la imagen.')

        updated_audio = request.form.get('updatedAudio')
        if updated_audio:
            buffer = request.files.get('bufferAudio')
            if not buffer or not buffer.filename:
                return http_error_400('El campo de audio `bufferAudio` es necesario si se va a editar el audio.')

        cancion_dictionary = cancion_select_repository.get_urls_cancion(cancion)
        if not cancion_dictionary:
            return http_error_400('Esta canción no existe.')

        if updated_picture:
            buffer = request.files.get('buffer')
            s3_upload_photo(buffer, cancion_dictionary.get('url_s3_foto'), True)

        if updated_audio:
            buffer = request.files.get('bufferAudio')
            s3_upload_audio(buffer, cancion_dictionary.get('url_s3_mp3'), True)

        cancion_update_repository.update_cancion(
            nombre,
            duracion,
            cancion
        )

        return http_ok_message_200('Canción actualizada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar actualizar una canción.')


def set_album_cancion(cancion):
    try:
        album = request.form.get('album')
        if not album:
            return http_error_400('El campo `album` es obligatorio.')

        cancion_update_repository.update_album_cancion(
            album,
            cancion
        )

        return http_ok_message_200('Canción agregada a álbum correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar agregar una canción a un álbum.')


def unset_album_cancion(cancion):
    try:
        cancion_update_repository.update_album_cancion(
            None,
            cancion
        )

        return http_ok_message_200('Canción removida de álbum correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar remover una canción de un álbum.')
