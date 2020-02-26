import os
import io
import logging
import boto3
from botocore.exceptions import ClientError
import json

# carregar client S3
s3_client = boto3.client('s3')

def main(event, context):
    
    records = []
    # verifica se é um objeto ou uma matriz de objetos
    if not isinstance(event, list):
        records = [event]
    else:
        records = event

    # inicializa variavel de retorno
    result = []

    # iterar
    for payload in records:

        # verifica variáveis do payload
        if 'bucket' not in payload:
            raise Exception("S3 Bucket not found")
        if 'path' not in payload:
            raise Exception("S3 Path not found")
        if 'object' not in payload:
            raise Exception("S3 Object not found")

        # monta o caminho para o s3
        s3_bucket = payload['bucket']
        s3_path = os.path.join(payload['path'], payload['object'])

        print("BUCKET S3: " , s3_bucket)
        print("PATH S3: " , s3_path)
        
        # tenta acessar um objeto S3
        contents = None
        try:
            s3_response = s3_client.get_object(Bucket=s3_bucket, Key=s3_path.lower())
            print('SUCCESS!')

            # lê conteudo do objeto
            # bytes_buffer = io.BytesIO()
            # s3_client.download_fileobj(Bucket=s3_bucket, Key=s3_path.lower(), Fileobj=bytes_buffer)
            # byte_value = bytes_buffer.getvalue()
            # contents = byte_value.decode() #python3, default decoding is utf-8

            # # contents = json.loads(s3_response['Body'].read())
            # print('content... ')
            # print(contents)

            dict_result = {"status":"200", "message":s3_response, "error": None}

            # guarda resultado bem sucedido
            result.append(dict(dict_result))
        except ClientError as e:
            print('FAILURE...')
            # logging.error(e)
            # guarda resultado com erros
            # dict_result = {"status":"600", "message":None, "error": e}
            # result.append(dict_result)

    return result