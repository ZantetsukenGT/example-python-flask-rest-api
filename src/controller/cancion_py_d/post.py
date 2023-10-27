from traceback import format_exc
from logging import error as log_error

from flask import request
from src.helper.http_response import http_ok_json_200, http_ok_message_200, http_error_400, http_error_500

from src.helper.s3 import upload_photo as s3_upload_photo
from src.helper.s3 import upload_audio as s3_upload_audio
from uuid import uuid4

import src.repository.cancion.insert as cancion_insert_repository

def post():
    try:
        nombre = request.form.get('nombre')
        if not nombre:
            return http_error_400('El campo `nombre` es obligatorio.')

        artista = request.form.get('artista')
        if not artista:
            return http_error_400('El campo `artista` es obligatorio.')

        duracion = request.form.get('duracion')
        if not duracion:
            return http_error_400('El campo `duracion` es obligatorio.')

        buffer1 = request.files.get('foto')
        if not buffer1 or not buffer1.filename:
            return http_error_400('El campo de imagen `foto` es obligatorio.')

        buffer2 = request.files.get('track')
        if not buffer2 or not buffer2.filename:
            return http_error_400('El campo de audio `track` es obligatorio.')

        album = request.form.get('album')
        if not album:
            album = None

        file_extension = buffer1.filename.split('.')[-1]
        filename = f'{str(uuid4())}.{file_extension}'
        url_s3_foto = s3_upload_photo(buffer1, filename, False)

        file_extension = buffer2.filename.split('.')[-1]
        filename = f'{str(uuid4())}.{file_extension}'
        url_s3_audio = s3_upload_audio(buffer2, filename, False)

        cancion_insert_repository.register_cancion(
            nombre,
            url_s3_foto,
            url_s3_audio,
            artista,
            duracion,
            album
        )

        return http_ok_message_200('Canción registrada correctamente.')
    except Exception:
        log_error(format_exc())
        return http_error_500('Error del servidor al intentar registrar una canción.')
