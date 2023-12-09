from fastapi import APIRouter, Depends, Request
from fastapi.security import OAuth2PasswordRequestForm
from service.ServiceAuth import validarUsuario
from utils.logback import logging

router = APIRouter(
    tags=['Autenticacion']
)

@router.post('/login')
def login(request: Request, usuario: OAuth2PasswordRequestForm = Depends()):
    respuesta = validarUsuario(usuario)
    
    url = request.url
    method = request.method
    response = "Proceso LOGIN DE USUARIO terminado satisfactoriamente"
    logging.info(f'URL: [{url}] - Metodo: [{method}] ---> Respuesta: {response}')
    
    return respuesta