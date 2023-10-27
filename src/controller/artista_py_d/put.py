from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo

import src.repository.artista.select as artista_select_repository
import src.repository.artista.update as artista_update_repository

def put(artista):
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        updated_picture = request.form.get('updatedPicture')
        if updated_picture:
            buffer = request.files.get('buffer')
            if not buffer or not buffer.filename:
                return http_error_400('El campo de imagen `buffer` es necesario si se va a editar la imagen.')

        artista_dictionary = artista_select_repository.get_url_artista(artista)
        if not artista_dictionary:
            return http_error_400('Este artista no existe.')

        if updated_picture:
            buffer = request.files.get('buffer')
            s3_upload_photo(buffer, artista_dictionary.get('url_s3_foto'), True)

        artista_update_repository.update_artista(
            nombre,
            artista
        )

        return http_ok_message_200('Artista actualizado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar actualizar un artista.')
