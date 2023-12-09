from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database.connection import Base

class ToPersona(Base):
    __tablename__ = 'to_persona'

    id_persona = Column(Integer, primary_key=True, index=True)
    fc_nombre = Column(String(50), nullable=False)
    fc_primer_apellido = Column(String(50))
    fc_segundo_apellido = Column(String(50))
    fc_correo = Column(String(50))
    fi_estatus_registro = Column(Integer, nullable=False)
    fd_fecha_creacion = Column(DateTime, nullable=False)
    
    to007_usuario = relationship('ToUsuario', back_populates="to007_persona")