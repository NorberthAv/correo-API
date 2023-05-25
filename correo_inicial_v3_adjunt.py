import smtplib, ssl
import getpass

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

destinatario = "norberthavilan@gmail.com"
username = "enviocorreomed@gmail.com"
password = "jjhadtfthdblstpr"

asunto  = "Mensaje de Solicitud de Cita"
mensaje = MIMEMultipart("alternative")
mensaje["Subject"] = f"Solicitud de Cita de {username}"
mensaje["From"] = username
mensaje["To"] = destinatario

html = f"""
<html> 
<body> mensaje de base de datos <br>
<p>{destinatario}</p>
</body>
</html>
"""

archivo = "img/rosas.jpg"

with open(archivo,"rb") as adjunto:
    contenido_adjunto = MIMEBase("application", "octet-stream")
    contenido_adjunto.set_payload(adjunto.read())

encoders.encode_base64(contenido_adjunto)

contenido_adjunto.add_header(
    "Content-Disposition",
    f"attachment; filename={archivo}",
)
mensaje.attach(contenido_adjunto)

parte_html = MIMEText(html,"html")

mensaje.attach(parte_html)

text = mensaje.as_string()
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("correo enviado")
    server.sendmail(username, destinatario, text)
    print("mensaje enviado")