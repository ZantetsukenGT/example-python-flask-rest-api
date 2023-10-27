from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo

import src.repository.album.select as album_select_repository
import src.repository.album.update as album_update_repository

def put(album):
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        descripcion = request.form.get('descripcion')
        if not descripcion:
            return http_error_400('El campo `descripcion` es obligatorio.')

        updated_picture = request.form.get('updatedPicture')
        if updated_picture:
            buffer = request.files.get('buffer')
            if not buffer or not buffer.filename:
                return http_error_400('El campo de imagen `buffer` es necesario si se va a editar la imagen.')

        album_dictionary = album_select_repository.get_url_album(album)
        if not album_dictionary:
            return http_error_400('Este album no existe.')

        if updated_picture:
            buffer = request.files.get('buffer')
            s3_upload_photo(buffer, album_dictionary.get('url_s3_foto'), True)

        album_update_repository.update_album(
            nombre,
            descripcion,
            album
        )

        return http_ok_message_200('Álbum actualizado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar actualizar un álbum.')
