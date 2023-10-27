from dotenv import load_dotenv
load_dotenv()  # cargar las variables de .env

# Revisa que existan las variables de entorno necesarias y si no, temina el programa
import src.config.db_config
import src.config.s3_config

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from src.controller.album import album_bp
from src.controller.artista import artista_bp
from src.controller.cancion import cancion_bp
from src.controller.favorito import favorito_bp
from src.controller.historial import historial_bp
from src.controller.playlist import playlist_bp
from src.controller.usuario import usuario_bp

app.register_blueprint(album_bp)
app.register_blueprint(artista_bp)
app.register_blueprint(cancion_bp)
app.register_blueprint(favorito_bp)
app.register_blueprint(historial_bp)
app.register_blueprint(playlist_bp)
app.register_blueprint(usuario_bp)
