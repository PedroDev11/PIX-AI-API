from common.hash import Hash
from utils.logback import logging
from service.modelo_respuesta import ModeloRespuesta

def verificarContrasena(fcContrasena, nuevaContrasena):
    if Hash.verify(fcContrasena, nuevaContrasena):
        mensaje = "Las contrasenas son iguales, la nueva contrasena no puede ser la misma que la anterior."
        logging.warning("Las contrasenas son iguales, la nueva contrasena no puede ser la misma que la anterior.")
        return "NOK", mensaje
    else:
        mensaje = "Las contraseñas no coinciden, puede acceder al cambio de contrasena"
        logging.info("Las contrasenas no coinciden. Puede acceder al cambio de contrasena")
        return "OK", mensaje
    