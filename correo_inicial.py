import smtplib, ssl
import getpass


username = "enviocorreomed@gmail.com"
password = "jjhadtfthdblstpr"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(username, password)
    print("correo enviado")
    destinatario = ('norberthavilan@gmail.com')
    mensaje = ('prueba de envio')
    server.sendmail(username, destinatario,mensaje)
    print("mensaje enviado")