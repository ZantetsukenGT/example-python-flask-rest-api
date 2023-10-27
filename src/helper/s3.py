import boto3
from src.config.s3_config import bucket

def upload_file(buffer, key):
    s3 = boto3.client("s3")

    s3.put_object(
        Bucket = bucket,
        Key = key,
        Body = buffer
    )
    return f'https://{bucket}.s3.amazonaws.com/{key}' 

def upload_photo(buffer, filename, update):
    if update:
        segments = filename.split('/')
        filename = segments[-1]

    filename = f'fotos/{filename}'

    return upload_file(buffer, filename)

def upload_audio(buffer, filename, update):
    if update:
        segments = filename.split('/')
        filename = segments[-1]

    filename = f'canciones/{filename}'

    return upload_file(buffer, filename)
