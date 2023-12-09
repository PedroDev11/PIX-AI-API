from database.connection import dbSession
from sqlalchemy.orm.session import Session
from utils.logback import logging
from models.to_usuario import ToUsuario
from models.to_persona import ToPersona

@dbSession
def validar(usuarioDTO, db: Session):
    validarCorreoDTO = db.query(ToUsuario).filter(ToUsuario.fc_usuario == usuarioDTO.fc_usuario).first()
    logging.warning("El correo ya se encuentra asociado a una cuenta")
    
    return validarCorreoDTO

@dbSession
def agregarUsuario(usuarioDTO, personaDTO, db: Session):
    try:
        # SE AGREGA LA PERSONA A LA SESION
        db.add(personaDTO)
        db.flush()
        logging.info("Se registro la persona correctamente")
             
        # SE OBTIENE EL ID DE LA PERSONA Y SE AGREGA EL USUARIO A LA SESION
        usuarioDTO.fk_id_persona = personaDTO.id_persona
        
        logging.info("Se registro el usuario correctamente")
        db.add(usuarioDTO)
        db.commit()
        
        estatus = "200"
        mensaje = "Se registro la usuario correctamente"
        return estatus, mensaje
        
    except Exception as e:
        db.rollback()
        print(str(e))
        
        logging.exception("No se pudo registrar al usuario en la base de datos")
        estatus = "500"
        mensaje = "No se pudo registrar la empresa en la base de datos"
        return estatus, mensaje