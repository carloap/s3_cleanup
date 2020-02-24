import os
import logging
import boto3

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

        # tenta acessar um objeto S3
        try:
            s3_response = s3_client.get_object(Bucket=s3_bucket, Key=s3_path.lower())

            # lê conteudo do objeto
            contents = s3_response['Body'].read()

            # guarda resultado bem sucedido
            result.append({"status":"200", "message":s3_response, "error": None, "contents": contents})
        except Exception as e:
            print('FAILURE...')
            # logging.error(e)
            # guarda resultado com erros
            result.append({"status":"600", "message":None, "error": e})

    return result