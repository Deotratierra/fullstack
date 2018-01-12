#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import environ

SENDER = environ["EMAIL_SENDER"]
PASSWORD = environ["EMAIL_PASSWORD"]

RECEIVERS = []
SUBJECT = "Email de prueba"
MESSAGE = "Esto es un email de prueba usando la biblioteca %s"


"""Envía un mensaje con varias bibliotecas.
Los parámetros de todas las funciones son similares:

:param sender: Correo desde donde envías el mensaje
:type sender: str

:param password: Contraseña del correo desde donde
    envías el mensaje
:type password: str

:param receivers: Lista de correos que recibirán el mensaje
:type receivers: list

:param message: Mensaje a enviar
:type message str

:param host: Host del servidor SMTP (opcional)
:type host: str

:param port: Puerto del servidor SMTP (opcional)
:type port: int
"""

# ============================================================

# ---   OPCIÓN 1   --- smtplib
# https://docs.python.org/3/library/smtplib.html#

from smtplib import SMTP, SMTPException

def send_smtplib(sender, password, receivers, subject, message,
                 host="smtp.gmail.com", port=587):
    _message = "From: <%s>\nTo: " % sender
    for rec in receivers:
        _message += "<%s>, " % rec
    _message += "\nSubject: %s\n" % subject
    _message += message

    try:
        server = SMTP(host, port)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receivers, _message)
    except SMTPException as e:
        print("Error enviando un mail con smtplib: %s" % e)
    else:
        print("Email enviado correctamente con smtplib")

# ============================================================

# ---   OPCIÓN 2   --- mailthon
# pip3 install Mailthon
# https://github.com/eugene-eeo/mailthon

from mailthon import postman, email

def send_mailthon(sender, password, receivers, subject, message,
                  host="smtp.gmail.com"):
    try:
        p = postman(host=host, auth=(sender, password))
        r = p.send(email(
                    content=u"%s" % message,
                    subject="%s" % subject,
                    sender="%s" % sender,
                    receivers=receivers
                )
            )
    except Exception as e:
        print("Error enviando un mail con mailthon: %s" % e)
    else:
        print("Email enviado correctamente con mailthon")

# ============================================================

# ---   OPCIÓN 3   --- sengrid
# En algunas plataformas como Heroku es obligatorio el uso de sendgrid, 
# el cual proporciona 10000 envíos mensuales en su capa gratuita.
# pip3 install sendgrid
# https://github.com/sendgrid/sendgrid-python

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Email, Mail, Content

SENDGRID_API_KEY = environ["SENDGRID_API_KEY"] # Necesitas una clave

def send_sendgrid(sender, api_key, receiver, subject, message):
    try:
        sg = SendGridAPIClient(apikey=api_key)
        from_email = Email(sender)
        subject = u"%s" % subject
        to_email = Email(receiver)
        content = Content("text/plain", message)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
    except Exception as e:
        print("Error enviando un mail con sendgrid: %s" % e)
    else:
        print("Email enviado correctamente con sengrid")

# ============================================================

if __name__ == "__main__":
    send_smtplib(SENDER, PASSWORD, RECEIVERS, SUBJECT, MESSAGE % "smtplib")
    send_mailthon(SENDER, PASSWORD, RECEIVERS, SUBJECT, MESSAGE % "mailthon")
    send_sendgrid(SENDER, SENDGRID_API_KEY, RECEIVERS[0], SUBJECT, MESSAGE % "sendgrid")
