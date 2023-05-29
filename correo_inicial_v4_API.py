import smtplib, ssl, base64
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
from email import encoders


app = Flask(__name__)
api = Api(app)

class EnviarCorreo(Resource):
    def post(self):
        
        data = request.form
        correo_paciente = data.get('correo_paciente')
        destinatarios = f"norberthavilan@gmail.com"
# isaacleonardomc@gmail.com
        # destinatario = "norberthavilan@gmail.com"



        username = "enviocorreomed@gmail.com"
        password = "jjhadtfthdblstpr"

        correo_cuerpo = data.get('cuerpo_correo')
        recipe = data.get('recipe')
        print(correo_paciente)
        # username = data.get('username')
        # password = data.get('password')
        # archivo = request.files.get('archivo')
    
        archivo_base64 = data.get('archivo')
        datos_adjunto = base64.b64decode(archivo_base64)

        mensaje = MIMEMultipart("alternative")
        mensaje["Subject"] = f"Solicitud de Cita de {username}"
        mensaje["From"] = username
        mensaje["To"] = f"{destinatarios},{correo_paciente}"

        html = f"""
        <html> 
        <body><h3>Solicitud de CITA</h3><br>
        {correo_cuerpo}
        </body>
        </html>
        """

        # with open(archivo.filename, "rb") as adjunto:
        #     contenido_adjunto = MIMEBase("application", "octet-stream")
        #     contenido_adjunto.set_payload(adjunto.read())

        # encoders.encode_base64(contenido_adjunto)

        contenido_adjunto = MIMEBase("application", "octet-stream")
        contenido_adjunto.set_payload(datos_adjunto)
        encode_base64(contenido_adjunto)

        # Agregar encabezados al archivo adjunto
        nombre_archivo = "archivo.pdf" # Nombre del archivo adjunto
        contenido_adjunto.add_header(
            "Content-Disposition",
            f"attachment; filename={nombre_archivo}",
        )
        mensaje.attach(contenido_adjunto)
        parte_html = MIMEText(html,"html")
        mensaje.attach(parte_html)

        text = mensaje.as_string()
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(username, password)
                server.sendmail(username, destinatarios, text)
                server.sendmail(username, correo_paciente, text)

             
        except Exception as e:
            # error_msg = str(e)
            # error_msg = 'error'
            return {'mensaje': 'Correo enviado correctamente', 'resp':'error'}
            # return jsonify({'mensaje': 'Error al enviar correo electrónico', 'error': error_msg}), 500

        return {'mensaje': 'Correo enviado correctamente', 'resp':'ok'}

api.add_resource(EnviarCorreo, '/enviar_correo')

if __name__ == '__main__':
   app.run(debug=True, host='127.0.0.1', port=8920)