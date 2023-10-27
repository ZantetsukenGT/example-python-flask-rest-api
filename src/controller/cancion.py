from flask import Blueprint, request

from src.controller.cancion_py_d.delete import delete
from src.controller.cancion_py_d.get    import get
from src.controller.cancion_py_d.post   import post
from src.controller.cancion_py_d.put    import update_cancion, set_album_cancion, unset_album_cancion

cancion_bp = Blueprint('cancion', __name__, url_prefix = '/api')

cancion_bp.add_url_rule('/eliminarCancion/<cancion>', 'eliminarCancion',  delete,              methods=['DELETE'])
cancion_bp.add_url_rule('/read',                      'read',             get,                 methods=['GET'])
cancion_bp.add_url_rule('/registrarCancion',          'registrarCancion', post,                methods=['POST'])
cancion_bp.add_url_rule('/editarCancion/<cancion>',   'editarCancion',    update_cancion,      methods=['PUT'])
cancion_bp.add_url_rule('/albumAgregar/<cancion>',    'albumAgregar',     set_album_cancion,   methods=['PUT'])
cancion_bp.add_url_rule('/albumEliminar/<cancion>',   'albumEliminar',    unset_album_cancion, methods=['PUT'])
