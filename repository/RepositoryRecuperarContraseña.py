from sqlalchemy.orm.session import Session
from database.connection import dbSession
from models.to_usuario import ToUsuario
from models.to_liga_validacion import ToLigaValidacion
from utils.logback import logging
from common.encriptarBase64 import generarLiga

@dbSession
def validarLiga(idLiga, db: Session):
    # BUSCANDO LA LIGA PARA PODER VALIDAR SI TIENE UN ESTATUS ACTIVO
    consultaLiga = db.query(ToLigaValidacion).filter(ToLigaValidacion.id_liga_validacion == idLiga).first()
    estatusRegistro = consultaLiga.fi_estatus_registro
    logging.info("Se encontro la LIGA correctamente")
    
    return estatusRegistro

@dbSession
def registrarLiga(ligaDTO, idUsuario, db: Session):
    try:
        
        # OBTENEMOS EL ID DE LA LIGA GENERADA
        db.add(ligaDTO)
        db.flush()
        idLiga = ligaDTO.id_liga_validacion
        
        # SE GENERA LA LIGA Y EL ENVIO DE CORREO
        link = generarLiga(idUsuario, idLiga)
        ligaDTO.fc_liga = link
        
        db.add(ligaDTO)
        db.commit()
        logging.info("Se registro la LIGA correctamente")
        
        return link
    
    except Exception as e:
        db.rollback()        
        logging.exception("Ocurrio un error al registrar la LIGA en la base de datos.")
        
@dbSession
def validarUsuario(fcCorreo, db: Session):
    consultaUsuario = db.query(ToUsuario).filter(ToUsuario.fc_usuario == fcCorreo).first()
    logging.info("Se encontró el correo del usuario para el envio del email")
    
    return consultaUsuario

@dbSession
def consultarFcContrasena(fiIdUsuario, db: Session):
    consultaUsuario = db.query(ToUsuario).filter(ToUsuario.id_usuario == fiIdUsuario).first()
    fcContrasena = consultaUsuario.fc_contrasena
    
    return fcContrasena

@dbSession
def actualizarContrasena(fiIdUsuario, idLiga, fc_contrasena, db: Session):
    try:
        # CONSULTAMOS EL USUARIO
        consultaUsuario = db.query(ToUsuario).filter(ToUsuario.id_usuario == fiIdUsuario).first()
        
        # ACTUALIZANDO LA CONTRASEÑA DEL USUARIO
        consultaUsuario.fc_contrasena = fc_contrasena
        
        # CAMBIANDO LA LIGA EN ESTATUS 0
        consultaLiga = db.query(ToLigaValidacion).filter(ToLigaValidacion.id_liga_validacion == idLiga).first()
        consultaLiga.fi_estatus_registro = 0
        
        db.add(consultaUsuario)
        db.commit()       
        
    except Exception as e:
        db.rollback()        
        logging.exception("Ocurrio un error al actualizar la contrasena del usuario en la base de datos.")
        