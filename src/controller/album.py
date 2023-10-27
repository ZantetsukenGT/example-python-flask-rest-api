from flask import Blueprint, request

from src.controller.album_py_d.delete import delete
from src.controller.album_py_d.get    import get
from src.controller.album_py_d.post   import post
from src.controller.album_py_d.put    import put

album_bp = Blueprint('album', __name__, url_prefix = '/api')

album_bp.add_url_rule('/eliminarAlbum/<album>', 'eliminarAlbum',  delete, methods=['DELETE'])
album_bp.add_url_rule('/read',                  'read',           get,    methods=['GET'])
album_bp.add_url_rule('/registrarAlbum',        'registrarAlbum', post,   methods=['POST'])
album_bp.add_url_rule('/editarAlbum/<album>',   'editarAlbum',    put,    methods=['PUT'])
