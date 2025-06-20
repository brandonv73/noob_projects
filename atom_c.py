import psutil
import smtplib
from email.mime.text import MIMEText
#Paso 1: Verificar el espacio en C:
def verificar_espacio(drive="C:\\"):
    uso = psutil.disk_usage(drive)
    porcentaje_libre = 100 - uso.percent
    return porcentaje_libre
#Paso 2: Enviar correo
def enviar_alerta(destinatario, mensaje):
    remitente = "" #Correo elecronico del remitente
    contraseña = "" #Clave app segura

    msg = MIMEText(mensaje)
    msg["Subject"] = "Alerta: Espacio en disco bajo"
    msg["From"] = remitente
    msg["To"] = destinatario

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(remitente, contraseña)
        servidor.send_message(msg)

#Paso 3: Integracion.

if __name__ == "__main__":
    umbral = 20 #Porcentaje de alerta
    espacio = verificar_espacio()

    if espacio < umbral:
        mensaje = f"Atencion: Solo queda {espacio: .2f}% de espacio libre en C:."
        enviar_alerta("", mensaje) #entre comillas el correo 
    else:
        print(f"Espacio suficiente: {espacio: .2f}% libre en C:.")
