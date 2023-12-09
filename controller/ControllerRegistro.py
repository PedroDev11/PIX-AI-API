from fastapi import APIRouter, Request
from schemas.Esquemas import UserRequest
from service.ServiceRegistro import registrarUsuario
from utils.logback import logging

router = APIRouter(
    prefix='/registro',
    tags=['API usuario']
)

@router.post('/crear')
def registrar_usuario(request: Request, usuario: UserRequest):
    respuesta = registrarUsuario(usuario)
    
    url = request.url
    method = request.method
    response = "Proceso REGISTRO DE USUARIO terminado satisfactoriamente"
    logging.info(f'URL: [{url}] - Metodo: [{method}] ---> Respuesta: {response}')
    
    return respuesta