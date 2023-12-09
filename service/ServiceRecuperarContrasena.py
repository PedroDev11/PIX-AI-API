from repository.RepositoryRecuperarContraseña import validarUsuario, actualizarContrasena, consultarFcContrasena, registrarLiga
from utils.logback import logging
from utils.generarCorreo import generaCorreo
from common.hash import Hash
from .modelo_respuesta import ModeloRespuesta
from .VerificarContrasena import verificarContrasena
from models.to_liga_validacion import ToLigaValidacion

# FECHA
import datetime
date = datetime.datetime.now()
fecha = date.strftime("%Y-%m-%d %H:%M:%S")

def enviarCorreo(fcCorreo):
    validarFcCorreo = validarUsuario(fcCorreo)
    
    if validarFcCorreo:
        idUsuario = validarFcCorreo.id_usuario
        fc_correo = validarFcCorreo.fc_usuario
        
        # MODELO PARA REGISTRAR LA LIGA
        ligaDTO = ToLigaValidacion(
            fk_id_usuario = idUsuario,
            fi_estatus_registro = 1,
            fd_fecha_creacion = fecha
        )
        
        # REGISTRO DE LA LIGA
        link = registrarLiga(ligaDTO, idUsuario)
        
        # GENERAR Y ENVIAR CORREO
        generaCorreo(fc_correo, link)
        
        # MODELO DE RESPUESTA
        estatus = "OK"
        mensaje = "Se envio el email correctamente."
        resultado = "Revise su bandeja de recibidos, ahí podré encontrar el correo que le hemos envíado."
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)

        return respuesta
    
    else:
        estatus = "NOK"
        mensaje = "No se encontro un usuario asociado con ese correo electronico."
        resultado = "Por favor, registra o crea una nueva cuenta con ese usuario."
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
        logging.warning("No se encontro un usuario asociado con ese correo electronico.")
        
        return respuesta
    
def recuperarContrasena(idUsuario, idLiga, nuevaContrasena):
    # CONSULTAMOS LA CONTRASEÑA DEL USUARIO  
    fcContrasena = consultarFcContrasena(idUsuario)
        
    # PRIMERO SE VALIDA QUE LA NUEVA CONTRASEÑA NO SEA IGUAL A LA ANTERIOR
    verificarFcContrasena, mensaje = verificarContrasena(fcContrasena, nuevaContrasena)
    
    if verificarFcContrasena == "NOK":
        return verificarFcContrasena, mensaje
    
    if verificarFcContrasena == "OK":
        fc_contrasena = Hash.bcrypt(nuevaContrasena)        
        actualizarContrasena(idUsuario, idLiga, fc_contrasena)
        return verificarFcContrasena, mensaje
        