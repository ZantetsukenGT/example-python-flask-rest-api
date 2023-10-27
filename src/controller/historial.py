from flask import Blueprint, request


from src.controller.historial_py_d.get    import get
from src.controller.historial_py_d.post   import post
from src.controller.historial_py_d.put    import put

historial_bp = Blueprint('historial', __name__, url_prefix = '/api')

historial_bp.add_url_rule('/getHistorial/<correo>', 'getHistorial',       get,    methods=['GET'])
historial_bp.add_url_rule('/registrarHistorial',    'registrarHistorial', post,   methods=['POST'])
historial_bp.add_url_rule('/update',                'update',             put,    methods=['PUT'])
