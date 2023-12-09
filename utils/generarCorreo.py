import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.logback import logging

import os
from dotenv import load_dotenv
load_dotenv()

def generaCorreo(fcCorreo, link):
    remitente = os.getenv('USER')
    destinatario = fcCorreo
    asunto = 'Recuperar Contraseña'

    msg = MIMEMultipart()
    msg['Subject'] = asunto
    msg['From'] = remitente
    msg['To'] = destinatario
    
    try:
        with open('templates/recuperarContrasena.html', 'r', encoding='utf-8') as archivo:
            html_template = archivo.read()
        
        # Interpola las variables en el HTML
        html_format = html_template.replace("{link}", link)
        
        #adjuntar contenido html
        msg.attach(MIMEText(html_format, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remitente, os.getenv('PASSWORD'))

        server.sendmail(remitente, 
                        destinatario,
                        msg.as_string())
        server.quit()
        logging.info(f"Se envio el email al usuario {fcCorreo} correctamente.")
        
    except Exception as e:
        logging.warning("Ocurrio un error al enviar el email al usuario.")
        print(str(e))

# pixaitoeveryone@gmail.com 
