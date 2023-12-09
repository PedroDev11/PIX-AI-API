from openai import OpenAI
from utils.logback import logging
from service.modelo_respuesta import ModeloRespuesta

def crear_imagen(descripcion):
    
    client = OpenAI(
        api_key="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"
    )
    client.models.list()

    try:
        logging.info("Generando imagen")
        
        respuesta = client.images.generate(
            prompt = descripcion,
            n = 1,
            size = "256x256"
        )
        
        return respuesta.data[0].url
    except Exception as e:
        logging.exception("Ocurrio un error al generar la imagen")
        
        estatus = "NOK"
        mensaje = "Ocurrio un error al generar la imagen."
        resultado = None
        respuesta = ModeloRespuesta(estatus, mensaje, resultado)
                
        return respuesta