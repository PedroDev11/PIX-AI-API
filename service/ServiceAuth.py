from fastapi import HTTPException, status
from repository.RepositoryAuth import buscarUsuario
from auth.jwt import create_access_token
from common.hash import Hash
from utils.logback import logging
from service.modelo_respuesta import ModeloRespuesta

def validarUsuario(usuario):
    user = buscarUsuario(usuario.username)
    
    if not user:
        estatus = "NOK"
        mensaje = "Credenciales inválidas"
        resultado = None
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("Credenciales inválidas")
                
        return respuesta
    
    fcCorreo = user.fc_usuario
    fcContrasena = user.fc_contrasena
    estatusRegistro = user.fi_estatus_registro
    fiIdUsuario = user.id_usuario
    
    if not Hash.verify(fcContrasena, usuario.password):
        estatus = "NOK"
        mensaje = "Contraseña incorrecta"
        resultado = None
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("Contraseña incorrecta")
                
        return respuesta
    
    if estatusRegistro == 1:
        logging.info("Creando token")
        access_token = create_access_token(data = {'fcCorreo': fcCorreo, 'fiIdUsuario': fiIdUsuario})
        response = {
            'access_token': access_token,
            'token_type': 'bearer',
            'fcCorreo': fcCorreo,
            'fiIdUsuario': fiIdUsuario
        }
        
    else:
        estatus = "NOK"
        mensaje = "Este usuario tiene un estatus ináctivo"
        resultado = None
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("Contraseña incorrecta")
                
        return respuesta
    
    return response
