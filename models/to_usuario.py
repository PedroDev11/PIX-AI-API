from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.connection import Base

class ToUsuario(Base):
    __tablename__ = 'to_usuario'

    id_usuario = Column(Integer, primary_key=True, index=True)
    fk_id_persona = Column(ForeignKey('to_persona.id_persona'))
    fc_usuario = Column(String(100), nullable=False, unique=True)
    fc_contrasena = Column(String(60))
    fi_estatus_registro = Column(Integer, nullable=False)
    fi_id_usuario_creacion = Column(Integer, nullable=False)
    fd_fecha_creacion = Column(DateTime, nullable=False)

    to007_persona = relationship('ToPersona', back_populates="to007_usuario")