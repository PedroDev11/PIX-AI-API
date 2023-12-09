
class ModeloRespuesta():
    def __init__(self, estatus, mensaje, resultado):
        self.estatus = estatus
        self.mensaje = mensaje
        self.resultado = resultado
        
    def to_json(self):
        return {
            "estatus": self.estatus,
            "mensaje": self.mensaje,
            "resultado": self.resultado
        }