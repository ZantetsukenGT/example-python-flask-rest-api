from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo
from uuid import uuid4

import src.repository.artista.insert as artista_insert_repository

def post():
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        buffer = request.files.get('buffer')
        if not buffer or not buffer.filename:
            return http_error_400('El campo de imagen `buffer` es obligatorio.')

        fecha = request.form.get('fecha')
        if not fecha:
            fecha = None

        file_extension = buffer.filename.split('.')[-1]
        filename = f'{str(uuid4())}.{file_extension}'
        url_s3_foto = s3_upload_photo(buffer, filename, False)

        artista_insert_repository.register_artista(
            nombre,
            url_s3_foto,
            fecha
        )

        return http_ok_message_200('Artista registrado correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar un artista.')
