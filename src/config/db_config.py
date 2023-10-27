from os import environ

host = environ.get('DB_HOST')
user = environ.get('DB_USER')
password = environ.get('DB_PASS')
database = environ.get('DB_DATABASE')

if host is None:
    print('Falta la variable de entorno `DB_HOST`\nTerminando programa...')
    raise SystemExit
if user is None:
    print('Falta la variable de entorno `DB_USER`\nTerminando programa...')
    raise SystemExit
if password is None:
    print('Falta la variable de entorno `DB_PASS`\nTerminando programa...')
    raise SystemExit
if database is None:
    print('Falta la variable de entorno `DB_DATABASE`\nTerminando programa...')
    raise SystemExit

db_config = {
    'user': user,
    'password': password,
    'host': host,
    'database': database,
    'raise_on_warnings': True
}
