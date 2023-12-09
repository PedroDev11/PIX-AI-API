# .\env\Scripts\activate.bat
# py -m uvicorn main:app --reload

from fastapi import FastAPI
from controller import ControllerRegistro, ControllerAuth, ControllerRecuperarContrasena, ControllerGenerarImagen
from models import to_usuario, to_persona, to_liga_validacion
from database.connection import engine

app = FastAPI()

app.include_router(ControllerRecuperarContrasena.router)
app.include_router(ControllerRegistro.router)
app.include_router(ControllerAuth.router)
app.include_router(ControllerGenerarImagen.router)

to_usuario.Base.metadata.create_all(engine)
to_persona.Base.metadata.create_all(engine)
to_liga_validacion.Base.metadata.create_all(engine)
