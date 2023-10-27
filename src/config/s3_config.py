from os import environ

region = environ.get('AWS_DEFAULT_REGION')
access_key_id = environ.get('AWS_ACCESS_KEY_ID')
secret_access_key = environ.get('AWS_SECRET_ACCESS_KEY')
bucket = environ.get('AWS_BUCKET_NAME')

if region is None:
    print('Falta la variable de entorno `AWS_DEFAULT_REGION`\nTerminando programa...')
    raise SystemExit
if access_key_id is None:
    print('Falta la variable de entorno `AWS_ACCESS_KEY_ID`\nTerminando programa...')
    raise SystemExit
if secret_access_key is None:
    print('Falta la variable de entorno `AWS_SECRET_ACCESS_KEY`\nTerminando programa...')
    raise SystemExit
if bucket is None:
    print('Falta la variable de entorno `AWS_BUCKET_NAME`\nTerminando programa...')
    raise SystemExit
