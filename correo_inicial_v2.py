import smtplib, ssl
import getpass

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
parte_html = MIMEText(html,"html")

mensaje.attach(parte_html)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("correo enviado")
    server.sendmail(username, destinatario, mensaje.as_string())
    print("mensaje enviado")