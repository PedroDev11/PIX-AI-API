from fastapi import APIRouter, Form, Request
from service.ServiceRecuperarContrasena import enviarCorreo, recuperarContrasena
from repository.RepositoryRecuperarContraseña import validarLiga
from common.encriptarBase64 import decryptBase
from utils.logback import logging
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags=['API recuperar contrasena']
)

# CONTROLADOR PARA EL ENVIO DE CORREO
@router.post('/recuperar-contrasena')
def enviar_correo(fcCorreo: str = Form(...)):
    respuesta = enviarCorreo(fcCorreo)
    return respuesta


# CONTRLADOR GET PARA EL INGRESO DE LA CONTRASEÑA
@router.get('/recuperar-contrasena/usuario', response_class=HTMLResponse)
def recuperar_contrasena(request: Request, liga: str):
    idLiga, idUsuario = decryptBase(liga)
    estatusRegistro = validarLiga(idLiga)
    
    if estatusRegistro == 1:
        return templates.TemplateResponse('ingresoContrasena.html', {'request': request})
    if estatusRegistro == 0:
        return templates.TemplateResponse('ligaConsumida.html', {'request': request})
    

# CONTROLADOR PARA LA ACTUALIZACION DE LA CONTRASEÑA
@router.post('/recuperar-contrasena/usuario', response_class=HTMLResponse)
def actualizar_contrasena(request: Request, liga: str, contraseña: str = Form(...)):
    idLiga, idUsuario = decryptBase(liga)
    respuesta, mensaje = recuperarContrasena(idUsuario, idLiga, contraseña)
    
    if respuesta == "NOK":
        return templates.TemplateResponse('ingresoContrasena.html', {'request': request, 'mensaje': mensaje})
    if respuesta == "OK":
        
        url = request.url
        method = request.method
        response = "Proceso RECUPERACION DE CONTRASENA terminado satisfactoriamente"
        logging.info(f'URL: [{url}] - Metodo: [{method}] ---> Respuesta: {response}')
        
        return templates.TemplateResponse('cambioContrasenaSuccess.html', {'request': request})
