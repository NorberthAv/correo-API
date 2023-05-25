from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
api = Api(app)

class EnviarCorreo(Resource):
    def post(self):
        data = request.form
        destinatario = "norberthavilan@gmail.com"
        username = "enviocorreomed@gmail.com"
        password = "jjhadtfthdblstpr"
        # destinatario = data.get('destinatario')
        # username = data.get('username')
        # password = data.get('password')
        # archivo = request.files.get('archivo')
        contenido_adjunto = ('archivo')



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

        # with open(archivo.filename, "rb") as adjunto:
        #     contenido_adjunto = MIMEBase("application", "octet-stream")
        #     contenido_adjunto.set_payload(adjunto.read())

        # encoders.encode_base64(contenido_adjunto)

        contenido_adjunto.add_header(
            "Content-Disposition",
            f"attachment; filename={archivo.filename}",
        )
        mensaje.attach(contenido_adjunto)
        parte_html = MIMEText(html,"html")
        mensaje.attach(parte_html)

        text = mensaje.as_string()
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(username, password)
                server.sendmail(username, destinatario, text)
        except Exception as e:
            error_msg = str(e)
            return jsonify({'mensaje': 'Error al enviar correo electrónico', 'error': error_msg}), 500

        return {'mensaje': 'Correo enviado correctamente'}

api.add_resource(EnviarCorreo, '/enviar_correo')

if __name__ == '__main__':
    app.run(debug=True)