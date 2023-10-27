from flask import Blueprint, request

from src.controller.favorito_py_d.delete import delete
from src.controller.favorito_py_d.get    import get
from src.controller.favorito_py_d.post   import post
from src.controller.favorito_py_d.put    import put

favorito_bp = Blueprint('favorito', __name__, url_prefix = '/api')

favorito_bp.add_url_rule('/eliminarFavorito/<correo>/<cancion>', 'delete',            delete, methods=['DELETE'])
favorito_bp.add_url_rule('/getFavorito/<correo>',                'getFavorito',       get,    methods=['GET'])
favorito_bp.add_url_rule('/registrarFavorito',                   'registrarFavorito', post,   methods=['POST'])
favorito_bp.add_url_rule('/update',                              'update',            put,    methods=['PUT'])
