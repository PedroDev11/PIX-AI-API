from fastapi import APIRouter, Form, Request
from service.ServiceGenerarImagen import crear_imagen
from utils.logback import logging

router = APIRouter(
    tags=['API imagen']
)

@router.post('/generar-imagen')
def generar_imagen(request: Request, descripcion: str = Form(...)):
    resultado = crear_imagen(descripcion)
    
    url = request.url
    method = request.method
    response = "Proceso GENERAR IMAGEN terminado satisfactoriamente"
    logging.info(f'URL: [{url}] - Metodo: [{method}] ---> Respuesta: {response}')

    return resultado
