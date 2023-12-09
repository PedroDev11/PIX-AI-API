from pydantic import BaseModel

# We request this
class UserRequest(BaseModel):
    fcNombre: str
    fcPrimerApellido: str
    fcSegundoApellido: str
    fcCorreo: str
    fcContrasena: str