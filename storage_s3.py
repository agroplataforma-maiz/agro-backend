import os

import boto3


AWS_BUCKET = os.getenv("AWS_BUCKET")
AWS_ENDPOINT = os.getenv("AWS_ENDPOINT")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_DEFAULT_REGION = os.getenv("AWS_DEFAULT_REGION", "auto")


s3_client = boto3.client(
    "s3",
    endpoint_url=AWS_ENDPOINT,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_DEFAULT_REGION,
    )


def subir_archivo(
    archivo,
    object_key: str,
    content_type: str,
):
    s3_client.upload_fileobj(
        archivo,
        AWS_BUCKET,
        object_key,
        ExtraArgs={
            "ContentType": content_type,
        },
    )

    return object_key


def generar_url_temporal(
    object_key: str,
    expiracion: int = 900,
):
    return s3_client.generate_presigned_url(
        "get_object",
        Params={
            "Bucket": AWS_BUCKET,
            "Key": object_key,
        },
        ExpiresIn=expiracion,
    )
