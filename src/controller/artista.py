from flask import Blueprint, request

from src.controller.artista_py_d.delete import delete
from src.controller.artista_py_d.get    import get
from src.controller.artista_py_d.post   import post
from src.controller.artista_py_d.put    import put

artista_bp = Blueprint('artista', __name__, url_prefix = '/api')

artista_bp.add_url_rule('/eliminarArtista/<artista>', 'eliminarArtista',    delete, methods=['DELETE'])
#artista_bp.add_url_rule('/obtenerArtistas',           'obtenerArtistas',    get,    methods=['GET'])
artista_bp.add_url_rule('/registrarArtista',          'registrarArtista',   post,   methods=['POST'])
artista_bp.add_url_rule('/editarArtista/<artista>',   'editarArtista',      put,    methods=['PUT'])
