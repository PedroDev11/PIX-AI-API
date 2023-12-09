import base64
from utils.logback import logging

BASE_URL = "http://localhost:8000/recuperar-contrasena/usuario?liga="

def generarLiga(idUsuario, idLiga):
    try:
        liga = f'idUsuario={idUsuario}|idLiga={idLiga}'
        data = base64.b64encode(liga.encode('utf-8')).decode('utf-8')
        fcLiga = f'{BASE_URL}{data}'
        logging.info("Se genero la liga correctamente.")
        
        return fcLiga
    except Exception as e:
        logging.warning("Ocurrio un error al generar la liga.")
        print(str(e))


def decryptBase(liga):
    try:
        LigaUsuario = base64.b64decode(liga.encode('utf-8')).decode('utf-8')
        idSeparados = LigaUsuario.split('|')
        idUsuario = int(idSeparados[0].split('=')[1])
        idLiga = int(idSeparados[1].split('=')[1])
        logging.info("Se desencripto la liga exitosamente")
       
        return idLiga, idUsuario
    except Exception as e:
        logging.warning("Ocurrio un error al desencriptar la liga.")
        print(str(e))

decryptBase("aWRVc3VhcmlvPTJ8aWRMaWdhPTg=")