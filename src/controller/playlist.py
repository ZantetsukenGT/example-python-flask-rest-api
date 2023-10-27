from flask import Blueprint, request

from src.controller.playlist_py_d.delete import delete_playlist, delete_cancion_playlist
from src.controller.playlist_py_d.get    import get_playlists, get_canciones_playlist
from src.controller.playlist_py_d.post   import registrar_playlist, registrar_detalle_playlist
from src.controller.playlist_py_d.put    import put

playlist_bp = Blueprint('playlist', __name__, url_prefix = '/api')

playlist_bp.add_url_rule('/eliminarPlaylist/<playlist>',           'eliminarPlaylist',      delete_playlist,            methods=['DELETE'])
playlist_bp.add_url_rule('/playlistEliminar/<playlist>/<cancion>', 'playlistEliminar',      delete_cancion_playlist,    methods=['DELETE'])
playlist_bp.add_url_rule('/obtnerPlaylist/<correo>',               'obtnerPlaylist',        get_playlists,              methods=['GET'])
playlist_bp.add_url_rule('/obtnerCancionPlaylist/<playlist>',      'obtnerCancionPlaylist', get_canciones_playlist,     methods=['GET'])
playlist_bp.add_url_rule('/registrarPlaylist',                     'registrarPlaylist',     registrar_playlist,         methods=['POST'])
playlist_bp.add_url_rule('/playlistAgregar',                       'playlistAgregar',       registrar_detalle_playlist, methods=['POST'])
#playlist_bp.add_url_rule('/editarPlaylist/<playlist>',             'editarPlaylist',        put,                        methods=['PUT'])
