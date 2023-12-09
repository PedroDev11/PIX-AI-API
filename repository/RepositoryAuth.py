# MODELOS
from models.to_usuario import ToUsuario

# DB
from sqlalchemy.orm import Session
from database.connection import get_db

from utils.logback import logging

def dbSession(decorated_function):
    def wrapper(*args, **kwargs):
        with next(get_db()) as db:
            return decorated_function(*args, db=db, **kwargs)
    return wrapper

@dbSession
def buscarUsuario(fcNombre, db: Session):
    consultarUsuario = db.query(ToUsuario).filter(ToUsuario.fc_usuario == fcNombre).first()
    logging.info("Consultando el usuario")
    
    return consultarUsuario
