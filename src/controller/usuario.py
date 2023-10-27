from flask import Blueprint, request


from src.controller.usuario_py_d.get    import get
from src.controller.usuario_py_d.post   import login, register
from src.controller.usuario_py_d.put    import put

usuario_bp = Blueprint('usuario', __name__, url_prefix = '/api')

usuario_bp.add_url_rule('/getUsuario/<correo>',    'getUsuario',       get,      methods=['GET'])
usuario_bp.add_url_rule('/login',                  'login',            login,    methods=['POST'])
usuario_bp.add_url_rule('/registrarUsuario',       'registrarUsuario', register, methods=['POST'])
usuario_bp.add_url_rule('/editarUsuario/<correo>', 'editarUsuario',    put,      methods=['PUT'])
