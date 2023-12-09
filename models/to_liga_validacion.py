from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from database.connection import Base

class ToLigaValidacion(Base):
    __tablename__ = 'to_liga_validacion'

    id_liga_validacion = Column(Integer, primary_key=True, index=True)
    fk_id_usuario = Column(ForeignKey('to_usuario.id_usuario'), nullable=False)
    fc_liga = Column(String(200))
    fi_estatus_registro = Column(Integer, nullable=False, server_default=text("1"))
    fd_fecha_creacion = Column(DateTime, nullable=False)

    to_usuario = relationship('ToUsuario')

