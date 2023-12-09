from repository.RepositoryRegistro import agregarUsuario, validar
from schemas.Esquemas import UserRequest
from models.to_usuario import ToUsuario
from models.to_persona import ToPersona
from common.hash import Hash
from .modelo_respuesta import ModeloRespuesta
from utils.logback import logging

# FECHA
import datetime
date = datetime.datetime.now()
fecha = date.strftime("%Y-%m-%d %H:%M:%S")

def registrarUsuario(usuario: UserRequest):
    usuarioDTO = ToUsuario(
        fc_usuario = usuario.fcCorreo,
        fc_contrasena = Hash.bcrypt(usuario.fcContrasena),
        fi_estatus_registro = 1,
        fi_id_usuario_creacion = 1,
        fd_fecha_creacion = fecha
    )
    
    personaDTO = ToPersona(
        fc_nombre = usuario.fcNombre,
        fc_primer_apellido = usuario.fcPrimerApellido,
        fc_segundo_apellido = usuario.fcSegundoApellido,
        fc_correo = usuario.fcCorreo,
        fi_estatus_registro = 1,
        fd_fecha_creacion = fecha
    )
    
    validarCorreo = validar(usuarioDTO)
    
    # VALIDANDO PERSONA
    if validarCorreo:
        estatus = "NOK"
        mensaje = "El correo del usuario ya ha sido registrado previamente"
        resultado = None
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("El correo del usuario ya ha sido registrado previamente")
                
        return respuesta
    
    # SE MANDAN LOS OBJETOS PARA REGISTRARLOS EN LA BASE DE DATOS
    estatus, mensaje = agregarUsuario(usuarioDTO, personaDTO)
    
    # MODELOS DE RESPUESTA 200
    if estatus == "200":
        estatus = "OK"
        mensaje = "Operacion realizada correctamente"
        resultado = mensaje
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.info("Operacion realizada correctamente")
        
        return respuesta
    
    # MODELOS DE RESPUESTA 500
    if estatus == "500":
        estatus = "ERROR"
        mensaje = "Error al transaccionar en base de datos"
        resultado = mensaje
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("Error al transaccionar en base de datos") 
    
        return respuesta
