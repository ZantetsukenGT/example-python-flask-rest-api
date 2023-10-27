# Instrucciones
## Crear entorno virtual (python3-venv)
```bash
# Solo una vez, por si no existe 
python3 -m venv .venv

```

## Activar entorno virtual (python3-venv)
```bash
# Siempre que no esté activo el entorno virtual
source .venv/bin/activate

```

## Instalar dependencias
```bash
pip install -r requirements.txt

```

## Ejecutar en modo debug
```bash
flask run --debug --host=127.0.0.1 --port 4000

```

## Ejecutar en modo produccion
```bash
# $ waitress-serve --port=<port> <module>:<app>
waitress-serve --port=4000 app:app

```

## Desactivar entorno virtual

```bash
deactivate

```
